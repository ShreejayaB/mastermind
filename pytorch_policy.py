## inspired from NN from https://github.com/egeromin/mastermind/
import torch
import torch.nn as nn
import numpy as np
import config
                    

np.random.seed(123)

class Policy(nn.Module):

    def __init__(self):
        super(Policy, self).__init__()
        self.guess_embed    = nn.Embedding(config.max_guesses+1, config.guess_embedding_size)
        self.feedback_embed = nn.Embedding(config.max_guesses+1, config.feedback_embedding_size)
        self.lstm_cell      = nn.LSTMCell(input_size = config.guess_embedding_size + config.feedback_embedding_size,
                                      hidden_size = config.lstm_hidden_size)
        self.fc             = nn.Linear(config.lstm_hidden_size, config.max_guesses)
        
    def forward(self, game_state):
        
        hidden = None
        cell_state = None
        for guess, feedback in game_state:
            guess_tensor      = torch.tensor(guess)
            feedback_tensor   = torch.tensor(feedback)
            guess_embedded    = self.guess_embed(guess_tensor)
            feedback_embedded = self.feedback_embed(feedback_tensor)
            combined_embedded = torch.cat([guess_embedded, feedback_embedded],
                                         axis=-1)
            # input of shape (seq_len, batch, input_size)
            combined_embedded = combined_embedded.reshape(1,-1)            
            if hidden == None:
                hidden, cell_state = self.lstm_cell(combined_embedded)
#                 print(hidden.shape, cell_state.shape)
            else:
                hidden, cell_state = self.lstm_cell(combined_embedded, (hidden, combined_embedded))
        
        logits = self.fc(hidden)
        
        logits = nn.functional.softmax(logits)
        return logits
                                                 

if __name__ == "__main__":
    from episode import Episode
    import numpy as np
    np.random.seed(123)
    p = Policy()
    e = Episode(p, "0000")
    x = p(e.generate())
    print(x.detach().numpy())