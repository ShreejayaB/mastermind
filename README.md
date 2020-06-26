# Can we make an RL agent play Mastermind?

[Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) is a popular code-breaking boardgame for two players which resembles Cows and Bulls. 

![mastermind](images/mastermind.png?raw=true "mastermind")

Contributors :

  - [Nithish Bolleddula](https://github.com/nithish08)
  
  - [Shreejaya Bharathan](https://github.com/ShreejayaB)

### Project Summary:

Using Reinforcement learning to train an agent to play the mastermind game. We implemented two algorithms
1. [Q-learning](Q-learning.ipynb)
1. [Policy Gradient method](Policy-gradient.ipynb)

### Components of Reinforcement Learning
- Environment : Mastermind game board	
- Agent : Plays a move guessing the pattern	
- Example state : State consits of all the guesses taken by the agent and feedbacks obtained from environment previously.
- Example reward : Tuple of (Number of colors guessed correctly in right position, Number of colors guessed but in wrong position) 

We have tried using Q-learning and policy gradient algortihms to make the agent play the game efficiently. 



Links to relevant sections:
- [Environment for Q-learning](environment.py) 
- [Q-learning agent](agent.py)
- [Training Q-learning agent](Q-learning.ipynb)
- [Policy Gradient approach](Policy-gradient.ipynb)
- [Final Presentation](Presentation.pdf)


Here is a link to a video we made to explain this project
[![Alt text for your video](https://img.youtube.com/vi/zjR_qvMhgB8/0.jpg)](https://youtu.be/zjR_qvMhgB8)


References:
-  An optimal mastermind strategy - https://arxiv.org/pdf/1305.1010.pdf
- https://en.wikipedia.org/wiki/Mastermind_(board_game)
- https://github.com/egeromin/mastermind/
- https://twitter.com/raymondh/status/1250998905984045056?lang=en