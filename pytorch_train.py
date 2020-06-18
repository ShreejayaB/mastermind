import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter
import random
import argparse
import os
import sys
import numpy as np

from episode import Episode
from pytorch_policy import Policy
import config



def save_model(m, p): torch.save(m.state_dict(), p)
def load_model(m, p): m.load_state_dict(torch.load(p))

def train(num_episodes=1000, 
          save_every=100, 
          checkpoint_dir="checkpoints",
          tensorboard_dir="tensorboard",
          tboard_every=10):
    
    pol = Policy()
    writer = SummaryWriter(log_dir=tensorboard_dir)
    G = -1
    optimizer = torch.optim.SGD( pol.parameters(),
                lr=-config.reinforce_alpha*G)
    criterion = nn.CrossEntropyLoss()
    pol.train
    total_step_count = 1
    print("step     loss")
    for j in range(1, num_episodes+1):
        random_secret = random.randint(0, config.max_guesses - 1)
        e = Episode(pol, random_secret)
        history = e.generate()

        print("Episode length: {}".format(len(history)))

        episode_loss = []
        for i in reversed(range(1, len(history))):
            history_so_far = history[:i]
            next_action, _ = history[i]
            
            action_logits = pol(history_so_far)
            loss = criterion( action_logits , torch.tensor(next_action).reshape(-1))
            optimizer.zero_grad()
            
            if j == num_episodes and i==len(history)-1:
                loss.backward()
            else:
                loss.backward(retain_graph=True)
            optimizer.step()
            episode_loss.append(loss)
            
            print(f"{total_step_count} - {loss}")
            writer.add_scalar('episode_loss', loss, total_step_count)
            total_step_count += 1

        
    if j % save_every == 0 or j == num_episodes:
        save_path = os.path.join(checkpoint_dir, 
                                 "episode{}".format(
                                     str(j).zfill(len(str(num_episodes)))))
        save_model(pol, save_path)

    if j % tboard_every == 0:
        writer.add_scalar('avg_episode_loss', 
                           torch.tensor([np.mean(episode_loss)]), 
                            j)
            
            
            
            
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train the mastermind model "
                                     "Using the REINFORCE policy gradient "
                                     "method")
    parser.add_argument("--num_episodes", 
                        help="Number of episodes to use for training",
                        type=int, default=1000)
    parser.add_argument("--save_every", type=int, default=100,
                        help="Checkpoint every N episodes")
    parser.add_argument("--checkpoint_dir", help="Checkpoint directory",
                        default="checkpoints")
    parser.add_argument("--board_dir", help="Tensorboard directory",
                        default="tensorboard")
    parser.add_argument("--tboard_every", type=int, default=10,
                        help="Write to tensorboard every N episodes")
    args = parser.parse_args()
                                  
    train(args.num_episodes, args.save_every, args.checkpoint_dir,
          args.board_dir, args.tboard_every)

