import config
import numpy as np
import itertools
import random
from collections import Counter


class Environment:
    '''Environment for mastermind game'''
    def __init__(self, secret):
        if isinstance(secret, int):
            secret = self._number_from_index(secret)
        self.secret = secret

    @staticmethod
    def _index_from_number(number):
        """
        Convert a 4-digit guess to an index between 0 and 6**4 -  1
        0 = 0000
        1 = 0001
        .
        .
        .
        6**4-1 = 5555
        """
        assert(len(number) <= 4)
        assert(set(number) <= set(map(str, range(6))))
        return int(number, base=6)

    @staticmethod
    def _number_from_index(index):
        '''inverse of _index_from_number function'''
        assert(0 <= index < config.max_guesses)
        digits = []
        while index > 0:
            digits.append(str(index % 6))
            index = index // 6
        return "".join(reversed(digits)).zfill(4)
    
    @staticmethod
    def score(p, q):
        '''feedback given during the mastermind game'''
        hits = sum(p_i == q_i for p_i, q_i in zip(p, q))
        misses = sum((Counter(p) & Counter(q)).values()) - hits
        return hits, misses
    
    def get_feedback(self,action):
        '''feedback for the current guess and secret'''
        return self.score(self.secret, action)
    
    def reward(self, guess):
        '''returns reward for a guess'''
        if guess == self.secret:
            return 1
        else:
            return -1
         
    