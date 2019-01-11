# Maxim Shelopugin
# 10-armed bandit

import numpy as np
import gym
from gym import spaces
from gym.utils import seeding

class NArmedBandit(gym.Env):
# Initialize with 10 arms, gausssian means with mean = 0, variance = 1
    def __init__(self):
        self.bandits = 10
        self.means = []
        self.action_space = spaces.Discrete(self.bandits)
        self.observation_space = spaces.Discrete(1)
        self.seed_num = 1
        self.np_random = None
        self.seed(self.seed_num)

# Each action returns a random reward with mean = mean[a], variance = 1
    def step(self, action):
        assert self.action_space.contains(action)
        reward = self.np_random.gaussian(self.means[action],1)
        return 0, reward, True, {}

# Define the seed
    def seed(self, seed=1):
        self.seed_num = seed
        self.np_random, seed = seeding.np_random(seed)
        self.means = []
        for _ in range(self.bandits):
            self.means.append(self.np_random.gaussian(0,1))
        return [seed]

# Nothing to reset
    def reset(self):
        self.seed(self.seed_num)

# When rendering, print the true reward destribution
    def render(self, mode='human', close=False):
        print('{:10}'.format("True vals:"),end=" [")
        for dist in self.means:
        	print('%6.3f'%dist,end=' ')
        print("]")

    def getmax(self):
    	return np.max(self.means)