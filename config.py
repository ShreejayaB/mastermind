lstm_hidden_size = 256
feedback_embedding_size = 8
guess_embedding_size = lstm_hidden_size - 2*feedback_embedding_size
max_guesses = 6**4
max_feedback = 15
reinforce_alpha = 0.001
max_episode_length = 30
