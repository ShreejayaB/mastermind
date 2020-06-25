from environment import Environment
import random


class Agent:
    '''Q learning Agent'''
    def __init__(self, epsilon=0.1, alpha=1.0):
        self.initialize_V()
        self.epsilon = epsilon
        self.alpha = alpha
        self.reset_possible_states()
        
        
    
    def initialize_V(self):
        '''initializes State Value function with zeros'''
        self.V = {}
        for idx in range(0, 6**4):
            self.V[Environment._number_from_index(idx)] = 0

    def reset_possible_states(self):
        '''set of possible states for the next action'''
        self.possible_states = list(self.V.keys())
    
    def restrict_possible_states(self, guess, feedback):
        '''restrict the possible states according to previous guesses'''
        new_states = [state for state in self.possible_states if Environment.score(guess, state)==feedback]
        self.possible_states = new_states
        
    def learn_select_move(self):
        
        best_move = self.get_best_action()
        
        selected_move = best_move
        if random.random() < self.epsilon:
            selected_move = self.random_action()
        
        return (best_move, selected_move)
    
    def get_best_action(self):
        "For the best possible states, chose randomly amongst them."
        V_values = [self.V[state] for state in self.possible_states]
        max_V = max(V_values)
        chosen_state = random.choice([state for state in self.possible_states if self.V[state] == max_V])
        return chosen_state
    
    def random_action(self):
        return random.choice(self.possible_states)
    
    def make_move(self, action, feedback):
        self.restrict_possible_states(action, feedback)
        
    def learn_from_move(self, action, feedback, reward):
        "The heart of Q-learning."
        
        # TODO: Finish each line with code and comments
        current_state = action  # action = state (guess the agent makes)
        r = reward  # reward for this state

        
        self.make_move(action, feedback) ## restrict the states first
        
        best_next_move, selected_next_move = self.learn_select_move()  # Exploration vs exploitation
        
        current_state_value = self.V[current_state] # current value of state
        best_move_value = self.V[best_next_move]  # best possible value of next state.
        td_target = current_state_value + self.alpha * (r + best_move_value - 
                                                        current_state_value)  # Q-algorithm update
        self.V[current_state] = td_target # This is Q-learning. The previous lines setup this line. 
        