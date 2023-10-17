# Create a dictionary to represent the graph
graph = {
    'A': {'heuristic': 10, 'neighbors': {'F': 3, 'B': 6}}, 
    'B': {'heuristic': 8, 'neighbors': {'D': 2, 'C': 3}},
    'C': {'heuristic': 5, 'neighbors': {'B': 3, 'D': 1, 'E': 5}},
    'E': {'heuristic': 3, 'neighbors': {'I':5 , 'J': 5, 'D': 8 , 'C':5}},
    'D': {'heuristic': 7, 'neighbors': {'B': 2, 'C': 1, 'E': 8}},
    'F': {'heuristic': 6, 'neighbors': {'G': 1, 'H': 7}},
    'G': {'heuristic': 5, 'neighbors': {'I': 3}},
    'H': {'heuristic': 3, 'neighbors': {'I': 2}},
    'I': {'heuristic': 1, 'neighbors': {'E': 5, 'J': 3}},
    'J': {'heuristic': 0, 'neighbors': {'E': 5, 'I': 3}},
}

def find_min_weight(graph):

    min_weights = {}
    f = 0 
    for node ,All_Data in graph.items():
        min_weights_ = float('inf')
        min_weights_Node = None
        h = All_Data['heuristic'] 
        for node_ , weights_ in All_Data["neighbors"].items():
            if  weights_ < min_weights_ :
                min_weights_Node = node_
                h2  = graph[node_]['heuristic']
                min_weights_ = weights_ 
                f = h2 + min_weights_
                print(f) 
        min_weights[node] = {'MoveTo':min_weights_Node ,'Cost':min_weights_}    
        # break      
    return min_weights 








min_weights = find_min_weight(graph)
for node, data in min_weights.items():
    print(f"Minimum weight from {node} to {data['MoveTo']} is {data['Cost']}") 
