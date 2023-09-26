
class AdjNode:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Pointer to the next adjacent node in the list (initially None)

class Graph():
    def __init__(self, V):
        self.V  = V
        self.NumberofVertiex = [None] * self.V
    def AddNewNode(self , Start , End):
        Node = AdjNode(End)
        Node.next = self.NumberofVertiex[Start] 
        self.NumberofVertiex[Start] = Node
        Node = AdjNode(Start)
        Node.next = self.NumberofVertiex[End]
        self.NumberofVertiex[End] = Node 
    def delete_edge(self, start, end):
        if self.NumberofVertiex[start] is None:
            return
        if self.NumberofVertiex[start].data == end:
              self.NumberofVertiex[start] = self.NumberofVertiex[start].next
              return 
        currnet  = self.NumberofVertiex[start]
        while currnet.next:
            if currnet.next.data == end:
                currnet.next = currnet.next.next
                return
            currnet = currnet.next
    def get_connected_nodes(self, node):
        temp = self.NumberofVertiex[node]
        while temp:
            print(" -> {}".format(temp.data), end="")
            temp = temp.next
        print(" \n")
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.NumberofVertiex[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n") 
    def are_nodes_connected(self, v1, v2):
        if v1 in self.NumberofVertiex:
            if v2 in self.NumberofVertiex[v1]:
                return True
        return False
    def get_edge(self, node1, node2):
        if node1 in self.NumberofVertiex:
            for neighbor, weight in self.NumberofVertiex[node1]:
                if neighbor == node2:
                    return (node1, node2, weight) if weight is not None else (node1, node2)
        return None



    


if __name__ == "__main__":
    V = 5
    # Create graph and edges
    graph = Graph(V)
    graph.AddNewNode(0, 1) 
    graph.AddNewNode(0, 2)
    graph.AddNewNode(0, 4)
    graph.AddNewNode(0, 3)
    graph.print_agraph() 
    graph.delete_edge(0,1) 
    (graph.get_connected_nodes(0))
    print(graph.get_edge(0,2))
    print(graph.are_nodes_connected(0,1))
      