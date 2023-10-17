import heapq

class Node:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost # For heapq to compare nodes based on cost

def uniform_cost_search(graph, start, goal): # Dijkstra's algorithm
    visited = set() # Set of visited nodes
    priority_queue = [Node(start, 0)] # Priority queue to keep track of nodes to explore
    while priority_queue: # While there are nodes to explore
        node = heapq.heappop(priority_queue) # Get the node with the lowest cost form the priority queue
        current_state, current_cost = node.state, node.cost # Get the state and cost of the node

        if current_state == goal: # If the goal is reached, return the cost
            return current_cost 

        if current_state not in visited: # If the node has not been visited
            visited.add(current_state) # Add the node to the set of visited nodes

            for neighbor, cost in graph[current_state]: # For each neighbor of the current node 
                if neighbor not in visited: # If the neighbor has not been visited add it to the priority queue
                    heapq.heappush(priority_queue, Node(neighbor, current_cost + cost)) # Add the neighbor to the priority queue

    return None  # If no path is found
def main():
    
    graph = {
        'A': [('F', 3), ('B', 6)],
        'B': [('A', 6), ('C', 3),('D',2)],
        'C': [('D', 7), ('B', 3),('D',1)],
        'D': [('C', 1), ('E', 8),('D',2)],
        'E': [('D', 8), ('J', 7),('C',5),('I',5)],
        'F': [('A', 3), ('G', 1), ('H', 7)],
        'G': [('F', 1), ('I', 3)],
        'H': [('I', 6), ('F', 10)],
        'I': [('G', 3), ('H', 2), ('E', 5),('J',3)],
        'J': [('I', 3)]
    }


    start_node = 'A'
    goal_node = 'E'

    result = uniform_cost_search(graph, start_node, goal_node)
    if result is not None:
        print(f"Minimum cost from {start_node} to {goal_node} is {result}")
    else:
        print(f"No path found from {start_node} to {goal_node}")

if __name__ == "__main__":
    main()