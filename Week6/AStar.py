import heapq

def a_star(graph, start, goal):
    open_set = [(0, start)]  # Priority queue to keep track of nodes to explore
    g_scores = {node: float('inf') for node in graph}  # Cost from start to node
    g_scores[start] = 0 # Cost from start to start is 0
    f_scores = {node: float('inf') for node in graph} # Cost from start to node + heuristic from node to goal (f = g + h) 
    f_scores[start] = graph[start]['heuristic']  # Cost from start to start + heuristic from start to goal (f = g + h)
    came_from = {} # Parent node of each node
    while open_set:  # While there are nodes to explore
        _, current = heapq.heappop(open_set) # Get the node with the lowest cost form the priority queue
        if current == goal: # If the goal is reached, return the path
            path = [] 
            while current in came_from: # Reconstruct the path
                path.append(current)  # Add the current node to the path
                current = came_from[current] # Move to the parent node of the current node 
            path.append(start) # Add the start node to the path
            path.reverse() # Reverse the path
            return path # Return the path
        for neighbor, weight in graph[current]['neighbors'].items(): # For each neighbor of the current node 
            tentative_g_score = g_scores[current] + weight # Calculate the cost from start to the neighbor through the current node

            if tentative_g_score < g_scores[neighbor]: # If the cost from start to the neighbor through the current node is less than the cost from start to the neighbor
                came_from[neighbor] = current # Update the parent node of the neighbor
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = g_scores[neighbor] + graph[neighbor]['heuristic']
                heapq.heappush(open_set, (f_scores[neighbor], neighbor))

    return None

# Define the graph
graph = {
    'A': {'heuristic': 10, 'neighbors': {'F': 3, 'B': 6}}, 
    'B': {'heuristic': 8, 'neighbors': {'D': 2, 'C': 3}},
    'C': {'heuristic': 5, 'neighbors': {'B': 3, 'D': 1, 'E': 5}},
    'E': {'heuristic': 3, 'neighbors': {'I': 5, 'J': 5, 'D': 8, 'C': 5}},
    'D': {'heuristic': 7, 'neighbors': {'B': 2, 'C': 1, 'E': 8}},
    'F': {'heuristic': 6, 'neighbors': {'G': 1, 'H': 7}},
    'G': {'heuristic': 5, 'neighbors': {'I': 3}},
    'H': {'heuristic': 3, 'neighbors': {'I': 2}},
    'I': {'heuristic': 1, 'neighbors': {'E': 5, 'J': 3}},
    'J': {'heuristic': 0, 'neighbors': {'E': 5, 'I': 3}},
}

# Example usage
start_node = 'A'
goal_node = 'J'
path = a_star(graph, start_node, goal_node)

if path:
    print("Shortest path from", start_node, "to", goal_node, "is:", ' -> '.join(path))
else:
    print("No path found.")
