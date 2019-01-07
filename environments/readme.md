### Environments

#rl_bandit
- A 10-armed bandit playground
- The task is to maximize the reward, given a single state and 10 possible actions - namely, arms of a bandit
- Each arm has a mean reward which is chosen via a gaussian destribution with mean of 0 and variance of 1
- Each action taken results in a random reward, pulled from a gaussian destribution with mean of arm's mean and variance of 1
- To integrate the environment in gym, navigate to the folder with setup.py file, and type 'pip -install .'
- To use the environment in gym, import it via "import gym_n_bandit" and make it via gym.make('NArmedBandit')
- env.render() prints the means of each of the arms' rewards 

#rl_cliff_walker
- A gridworld with a cliff
- The task is to reach the goal state from the start state
- Start state is a coordinate on the grid = (3,0)
- Goal state is a coordinate on the grid = (3,9)
- State is represented by the tuple of x and y coordinate
- There are 4 actions = (Left, Down, Up, Right)
- Actions navigate the agent through the grid
- The agent cannot leave the area, so the action resulting in going out of bounds will have no effect
- Each time the agent makes a move, it recieves a reward -1
- If the agent moves to the cliff, the reward becomes -100, and the position of the agent is reset to a start state
- If the agent reaches the goal, the reward becomes +100
- To integrate the environment in gym, navigate to the folder with setup.py file, and type 'pip -install .'
- To use the environment in gym, import it via "import gym_cliff_walker" and make it via gym.make('CliffWalker')
- env.render() prints current gridworld statespace

#rl_windy_world
- A gridworld with a windy region
- The task is to reach the goal state from the start state
- Start state is a coordinate on the grid = (3,0)
- Goal state is a coordinate on the grid = (3,7)
- State is represented by the tuple of x and y coordinate
- There are 4 actions = (Left, Down, Up, Right)
- Actions navigate the agent through the grid
- The agent cannot leave the area, so the action resulting in going out of bounds will have no effect
- Each time the agent makes a move, it recieves a reward -1
- If the agent reaches the goal, the reward becomes +100
- If the agent enters the wind area, each following action will incur the displacement in negative y direction
- If the wind area is strong, the displacement = 2, otherwise the displacement = 1
- To integrate the environment in gym, navigate to the folder with setup.py file, and type 'pip -install .'
- To use the environment in gym, import it via "import gym_windy_world" and make it via gym.make('WindyGridworld')
- env.render() prints current gridworld statespace
