import heapq

# Define the grid
grid = [
    ['S', '.', '.', 'X', 'X'],
    ['.', 'X', '.', '.', '.'],
    ['.', 'X', 'X', '.', 'X'],
    ['.', '.', '.', '.', '.'],
    ['X', '.', 'X', 'X', 'G'] 
]

# Define the possible movement directions (up, down, left, right)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def heuristic(point, goal):
    # Calculate the Manhattan distance between the current point and the goal
    return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

def a_star_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {} 
    g_score = {point: float('inf') for row in grid for point in row}
    g_score[start] = 0
    f_score = {point: float('inf') for row in grid for point in row}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path
        
        for i, j in directions:
            neighbor = current[0] + i, current[1] + j
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != 'X':
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    if neighbor not in [node[1] for node in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

start_point = (0, 0)  # Replace with the actual start point coordinates
goal_point = (4, 4)   # Replace with the actual goal point coordinates

shortest_path = a_star_search(grid, start_point, goal_point)
if shortest_path:
    print("Shortest Path:")
    for point in shortest_path:
        print(point)
else:
    print("No path found.") 
