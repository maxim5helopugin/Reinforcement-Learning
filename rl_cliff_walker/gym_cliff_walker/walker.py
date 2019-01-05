import numpy as np
import gym
from gym import spaces

class CliffWalker(gym.Env):
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
		self.goal_reward = 100
		self.action_space = spaces.Discrete(4)

	def step(self, action):
		reward = 0
		done = False

		if action == 0:
			self.posy-=1
		if action == 1:
			self.posx+=1
		if action == 2:
			self.posy+=1
		if action == 3:
			self.posx-=1

		if self.posx < 0:
			self.posx = 0
		if self.posx > 3:
			self.posx = 3
		if self.posy < 0:
			self.posy = 0
		if self.posy > 9:
			self.posy = 9

		if self.on_cliff():
			reward = self.cliff_reward
			self.posx = 3
			self.posy = 0
		elif self.is_goal():
			reward = self.goal_reward
			done = True
		else:
			reward = self.reg_reward

		return (self.posx, self.posy), reward, done, {}

	def on_cliff(self):
		if self.posx==3 and (self.posy!=0 and self.posy!=9):
			return True
		return False

	def is_goal(self):
		if self.posx == self.rewx and self.posy == self.rewy:
			return True
		return False

	def reset(self):
		self.posx = 3
		self.posy = 0

	def render(self, mode='human', close=False):
		self.grid[self.posx][self.posy] = 'O'
		for row in self.grid:
			print(row)
		print()
		self.grid[self.posx][self.posy] = '_'
