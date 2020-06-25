# Can we make an RL agent play Mastermind?

[Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) is a popular code-breaking boardgame for two players which resembles Cows and Bulls. 

![mastermind](images/mastermind.png?raw=true "mastermind")

Overall Summary:

Using Reinforcement learning to train an agent to play the mastermind game.

			
- Environment : Mastermind game board	
- Agent : Plays a move guessing the pattern	
- Example state : State consits of all the guesses taken by the agent and feedbacks obtained from environment previously.
- Example reward : Tuple of (Number of colors guessed correctly in right position, Number of colors guessed but in wrong position) 

We have tried using Q-learning and policy gradient algortihms to make the agent play the game efficiently. 


Links to relevant sections:
- Q Learning 
- Training notebook 
- Policy Gradient approach


Contributors :

  - [Nithish Bolleddula](https://github.com/nithish08)
  
  - [Shreejaya Bharathan](https://github.com/ShreejayaB)

Here is a link to a video we made for this project
(REPLACE WITH ACTUAL LINK!!!! format [![Alt text for your video](https://img.youtube.com/vi/VIDEO-ID/0.jpg)](http://www.youtube.com/watch?v=VIDEO-ID))


References:
-  An optimal mastermind strategy - https://arxiv.org/pdf/1305.1010.pdf
- https://en.wikipedia.org/wiki/Mastermind_(board_game)
- https://github.com/egeromin/mastermind/
- https://twitter.com/raymondh/status/1250998905984045056?lang=en