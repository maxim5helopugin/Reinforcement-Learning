# Maxim Shelopugin
# Cliff Walker
import numpy as np
import gym
from gym import spaces
from gym.utils import seeding
import os

class CliffWalker(gym.Env):
# Initialize the grid, start pos = (3,0), goal pos = (3,9)
	def __init__(self):
		self.grid = [
	    	list("__________"),
	    	list("__________"),
	    	list("__________"),
	    	list("_XXXXXXXXG")
			]

		self.posx = 3
		self.posy = 0
		self.rewx = 3
		self.rewy = 9
		self.reg_reward = -1
		self.cliff_reward = -100
		self.goal_reward = 0
		self.action_space = spaces.Discrete(4)
		self.observation_space = spaces.Discrete(40)
		self.seed_num = 1
		self.np_random = None
		self.seed(self.seed_num)

# Each action results in -1 reward, unless it reaches goal, or the cliff
	def step(self, action):
		reward = 0
		done = False

# Action adjustment
		if action == 0:
			self.posy-=1
		if action == 1:
			self.posx+=1
		if action == 2:
			self.posy+=1
		if action == 3:
			self.posx-=1

# Dont leave the bounds
		if self.posx < 0:
			self.posx = 0
		if self.posx > 3:
			self.posx = 3
		if self.posy < 0:
			self.posy = 0
		if self.posy > 9:
			self.posy = 9

# On-cliff = reset position, get negative reward
		if self.on_cliff():
			reward = self.cliff_reward
			self.posx = 3
			self.posy = 0
			done = True

# Goal state = mark game as done, get reward
		elif self.is_goal():
			reward = self.goal_reward
			done = True
		else:
			reward = self.reg_reward

		return (self.posx*10+self.posy), reward, done, {}

# Check if on cliff
	def on_cliff(self):
		if self.posx==3 and (self.posy!=0 and self.posy!=9):
			return True
		return False

# Check if on goal
	def is_goal(self):
		if self.posx == self.rewx and self.posy == self.rewy:
			return True
		return False

# Reset position
	def reset(self):
		self.posx = 3
		self.posy = 0
		self.seed(self.seed_num)
		return self.posx*10+self.posy

# Render the environment
	def render(self, mode='human', close=False):
		self.grid[self.posx][self.posy] = 'O'
		for row in self.grid:
			print(row)
		print()
		self.grid[self.posx][self.posy] = '_'

# Define the seed
	def seed(self, seed=1):
		self.seed_num = seed
		self.np_random, seed = seeding.np_random(seed)
		return seed