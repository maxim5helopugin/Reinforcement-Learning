from gym.envs.registration import register
from .bandit import NArmedBandit

register(
	id='NArmedBandit-v0',
	entry_point='gym_n_bandit:NArmedBandit',
)
