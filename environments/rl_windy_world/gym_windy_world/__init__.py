from gym.envs.registration import register
from .wgridworld import WindyGridworld

register(
	id='WindyGridworld-v0',
	entry_point='gym_windy_world:WindyGridworld',
)
