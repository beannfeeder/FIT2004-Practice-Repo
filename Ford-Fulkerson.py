
#classes
#GRAPH - one way
class Graph:
    """
    A class to represent a directed graph using adjacency list representation.
    """
    def __init__(self, nodes):
        self.adj = [[] for _ in range(len(nodes))] #adjacency list
        
    def graph_add_edge(self, Edge):
        pass
    
    def ford_fulkerson(self): 
        # Placeholder for implementation
        print("test")
        pass
        #approach: residual network
        #start from 0 flow
        #bfs
        """
        
        current_flow = min(path_capacity)
        for i in path:
            update flow of all edges to current_flow
        """
        #augment path
        #if can't augment anymore, stop
        #return max_flow


#NODE - id, name, neighbours, weight
class Node:
    def __init__(self, id, edges):
        """
        Function Description: creates a node class and initializes its properties
        """
        # id = id of the node
        self.id = id
        self.edges = edges # list of edges connecting this node to other nodes

#Res_Node: id, name, neighbours, weight, flow
class RES_Node:
    def __init__(self, id):
        """
        Function Description: creates a node class and initializes its properties for residual graph
        """
        self.id = id
        self.edges = []
        self.previous = None #previous node, 
class Edge:
    def __init__(self, x, y, w):
        """
        Function Description: creates an edge class and initializes its properties
        """
        # x = node 1, y = node 2, w = weight
        self.source = x # source node
        self.target = y # target node
        self.capacity = w # weight of the edge      

class RES_EDGE:
    def __init__(self, x, y, w):
        """
        Function Description: creates an edge class and initializes its properties for residual graph
        """
        # x = node 1, y = node 2, w = weight
        self.source = x # source node
        self.target = y # target node
        self.capacity = w
        self.flow = 0 # current flow of the edge


#methods
# FORD FULKERSON
print("ford fulkerson")
apple = [[1, 2, 3, 5], [2,4,5,6]]
for index in apple:
    print(index)
print(apple)

"""
Simple question:
     2         
  A --- C---  
 /2         \ 2
S            F           from intuition, it should be 2 + 1, SACF can hold 2, SBDF can hold 1
 \ 3   1     /
   \- B----D/ 3
"""