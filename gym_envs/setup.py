from setuptools import setup

setup(name='gym_envs',
      version='0.0.1',
      install_requires=['gym'],
      packages = ['gym_envs', 'gym_envs.envs']
)  