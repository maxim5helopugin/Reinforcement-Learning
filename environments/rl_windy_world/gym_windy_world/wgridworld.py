# Maxim Shelopugin
# Windy Gridworld
import numpy as np
import gym
from gym import spaces

class WindyGridworld(gym.Env):
# Initialize the grid, wind locations, start = (3,0), goal = (3,7)
	def __init__(self):
		self.grid = [
			list("__________"),
			list("__________"),
			list("__________"),
			list("_______G__"),
			list("__________"),
			list("__________"),
			list("__________")
			]
		self.posx = 3
		self.posy = 0
		self.rewx = 3
		self.rewy = 7
		self.reg_reward = -1
		self.goal_reward = 100
		self.action_space = spaces.Discrete(4)
		self.observation_space = spaces.Discrete(70)
		self.high_wind = [6,7]
		self.low_wind = [3,4,5,8]

# Each action changes the position of the agent
	def step(self, action):
		reward = 0
		done = False

# Add noise if in windy territory
		if self.posy in self.high_wind:
			self.posx-=2
		elif self.posy in self.low_wind:
			self.posx-=1

# Adjust position
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
		if self.posx > 6:
			self.posx = 6
		if self.posy < 0:
			self.posy = 0
		if self.posy > 9:
			self.posy = 9

# Got to the goal state?
		if self.posx == self.rewx and self.posy == self.rewy:
			done = True
			reward = self.goal_reward
		else:
			reward = -1

		return (self.posx,self.posy), reward, done, {}

# Reset the position of the agent 
	def reset(self):
		self.posx = 3
		self.posy = 0
		return 0

# Render the gridworld environment
	def render(self, mode='human', close=False):
		self.grid[self.posx][self.posy] = 'O'
		for row in self.grid:
			print(row)
		print()
		self.grid[self.posx][self.posy] = '_'