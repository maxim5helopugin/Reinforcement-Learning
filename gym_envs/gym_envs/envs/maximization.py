# Maxim Shelopugin
import numpy as np
import gym
from gym import spaces
from gym.utils import seeding

class MaxBias(gym.Env):
	def __init__(self):
		self.seed_num = 1
		self.np_random = None
		self.action_space = spaces.Discrete(2)
		self.observation_space = spaces.Discrete(1)
		self.states = np.zeros(4)
		self.current_state = 2
		self.reward = 0
		self.num_actions = 100
		self.means = []
		self.seed(self.seed_num)


	def step(self, action):
		assert self.action_space.contains(action)
		if action == 0:
			self.current_state+=1
		else:
			self.current_state-=1

		if self.current_state == 3:
			return self.current_state, self.reward, True, {}
		elif self.current_state == 0:
			return self.current_state, self.means[action], True, {}

		if self.current_state == 1:
			self.action_space = spaces.Discrete(self.num_actions)
		else:
			self.action_space = spaces.Discrete(2)
		return self.current_state, self.reward, False, {}

 
	def reset(self):
		self.current_state = 2
		self.action_space = spaces.Discrete(2)
		self.seed(self.seed_num)

	def seed(self, seed=1):
		self.seed_num = seed
		self.np_random, seed = seeding.np_random(seed)
		self.means = []
		for _ in range(self.num_actions):
			self.means.append(self.np_random.normal(-0.1,1))
		return [seed]

	def render(self, mode='human', close=False):
		print(self.current_state)
