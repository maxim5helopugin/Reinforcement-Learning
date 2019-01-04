import numpy as np
import gym
from gym import spaces

class CliffWalker(gym.Env):
    def __init__(self):

    def step(self, action):
        return 0, reward, True, {}

    def reset(self):
        return 0

    def render(self, mode='human', close=False):
