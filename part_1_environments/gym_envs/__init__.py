from gym.envs.registration import register

register(
    id='NArmedBandit-v0',
    entry_point='gym_envs.envs:NArmedBandit',
)

register(
    id='CliffWalker-v0',
    entry_point='gym_envs.envs:CliffWalker',
)

register(
    id='WindyWorld-v0',
    entry_point='gym_envs.envs:WindyWorld',
)

register(
    id='MaxBias-v0',
    entry_point='gym_envs.envs:MaxBias',
)