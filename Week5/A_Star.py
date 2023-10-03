import heapq
import copy

# Define the initial state and goal state
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
class PuzzleState:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state          
        self.parent = parent        
        self.action = action        
        self.depth = depth         
        self.cost = self.calculate_cost() 
    def calculate_cost(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_i, goal_j = divmod(self.state[i][j] - 1, 3)
                    cost += abs(i - goal_i) + abs(j - goal_j)
        return cost + self.depth 
    def __lt__(self, other):
        return self.cost < other.cost


actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
action_names = ['left', 'right', 'up', 'down']
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3
def generate_successors(node):
    successors = []
    x, y = None, None  
    for i in range(3):
        for j in range(3):
            if node.state[i][j] == 0:
                x, y = i, j
                break
    for dx, dy in actions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y):
            new_state = copy.deepcopy(node.state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            successors.append(PuzzleState(new_state, node, action_names[actions.index((dx, dy))], node.depth + 1))
    return successors

def a_star_search(initial_state, goal_state):
    open_set = [PuzzleState(initial_state)]
    closed_set = set()
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == goal_state:
            path = []
            while current_node: 
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            path.reverse() 
            return path
        closed_set.add(tuple(map(tuple, current_node.state)))
        for successor in generate_successors(current_node):
            if tuple(map(tuple, successor.state)) not in closed_set:
                heapq.heappush(open_set, successor)
    return None  # No solution found



solution_path = a_star_search(initial_state, goal_state)



if solution_path:
    for action, state in solution_path:
        print(f'Action: {action}')
        for row in state:
            print(row)
        print('---')
else:
    print('No solution found.')
