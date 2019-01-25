# Reinforcement-Learning Repo
Repository to store reinforcement learning projects and experiments

# Bandits
- An experiment exploring different exploration techniques in a 10-armed Bandi environment
- Random exploration - choose an action randomly
- Epsilon-greedy exploration - choose a random action epsilon % of the time, otherwise choose the best action
- Softmax exploration - choose an action according to softmax distribution
- Upper Confidence Bound exploration - choose action with higher confidence, depending on the amount of tries for the action
- Thompson exploration - choose an action according to a beta destribution
- 10-pull exploration - pull each arm 10 times, proceed greedily after
- Double-q bandits - use two separate value approximators for more robust performance

# Environments
- Collection of environments developed for OpenAI Gym
- 10-armed bandit - maximize the reward by chosing the best of 10 actions with gaussian reward destridubiton
- Cliff Walker - reach the goal state, without touching the cliff
- Windy World - reach the goal state, while dealing with noisy actions

# Tabular Methods
- Sarsa, Q-learning and double q-learning on different environments
- Cliff-walker - sarsa and q-learning comparison
- MaxBias - q-learning and double q-learning comparison

# Approximate Methods
- Reinforcement learning algorithms, with non-linear function approximators
- Lunar Lander Continuous - Policy Gradient solution to the Lunar Lander
- Lunar Lander Discrete - Deep Q Learning solution to the Lunar Lander
