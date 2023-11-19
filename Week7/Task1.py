import numpy as np

# Constants for grid and actions
GRID_SIZE = 4
NUM_STATES = GRID_SIZE * GRID_SIZE
NUM_ACTIONS = 4  # 0: Left, 1: Down, 2: Right, 3: Up

# Define the Frozen Lake environment
GRID = [
    'SFFF',
    'FHFF',
    'FFFF',
    'HFFG'
]

# Convert the grid to a list of characters
GRID = [list(row) for row in GRID]

# Define state transitions (dynamics)
def transition_probability(state, action, next_state):
    i, j = state // GRID_SIZE, state % GRID_SIZE
    next_i, next_j = next_state // GRID_SIZE, next_state % GRID_SIZE
    if next_i < 0 or next_i >= GRID_SIZE or next_j < 0 or next_j >= GRID_SIZE:
        return 0.0  # Invalid move
    if GRID[i][j] == 'H':
        return 0.0  # Cannot transition from a hole state
    if state == next_state:
        return 0.0  # Staying in the same state has zero probability
    if action == 0:  # Left
        return 1.0 if (i == next_i and j - 1 == next_j) else 0.0
    elif action == 1:  # Down
        return 1.0 if (i + 1 == next_i and j == next_j) else 0.0
    elif action == 2:  # Right
        return 1.0 if (i == next_i and j + 1 == next_j) else 0.0
    elif action == 3:  # Up
        return 1.0 if (i - 1 == next_i and j == next_j) else 0.0
    return 0.0

# Define rewards
def reward(state, action):
    i, j = state // GRID_SIZE, state % GRID_SIZE
    if GRID[i][j] == 'H':
        return -1.0  # Entering a hole state incurs a penalty
    elif GRID[i][j] == 'G':
        return 1.0  # Reaching the goal state
    else:
        return -0.1  # Small negative reward for other states

# Initialize the value function
V = np.zeros(NUM_STATES)
# Value Iteration
gamma = 0.9
epsilon = 1e-6
while True:
    delta = 0
    for s in range(NUM_STATES):
        v = V[s]
        max_action_value = -np.inf
        for a in range(NUM_ACTIONS):
            action_value = sum(
                transition_probability(s, a, next_s) * (reward(next_s, a) + gamma * V[next_s])
                for next_s in range(NUM_STATES)
            )
            if action_value > max_action_value:
                max_action_value = action_value
        V[s] = max_action_value
        delta = max(delta, abs(v - V[s]))
    if delta < epsilon:
        break

# Extract the optimal policy
optimal_policy = np.zeros(NUM_STATES, dtype=int)
for s in range(NUM_STATES):
    max_action_value = -np.inf
    best_action = -1
    for a in range(NUM_ACTIONS):
        action_value = sum(
            transition_probability(s, a, next_s) * (reward(next_s, a) + gamma * V[next_s])
            for next_s in range(NUM_STATES)
        )
        if action_value > max_action_value:
            max_action_value = action_value
            best_action = a
    optimal_policy[s] = best_action

# Display the optimal policy
optimal_policy_grid = ['LRUD'[action] for action in optimal_policy]
optimal_policy_grid = [optimal_policy_grid[i:i+GRID_SIZE] for i in range(0, NUM_STATES, GRID_SIZE)]
for row in optimal_policy_grid:
    print(' '.join(row))