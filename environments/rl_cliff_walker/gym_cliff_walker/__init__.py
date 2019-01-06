from gym.envs.registration import register
from .walker import CliffWalker

register(
	id='CliffWalker-v0',
	entry_point='gym_cliff_walker:CliffWalker',
)
