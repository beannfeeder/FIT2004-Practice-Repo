from collections import deque

#classes
#GRAPH - one way
class Graph:
    """
    A class to represent a directed graph using adjacency list representation.
    """
    def __init__(self, nodes):
        self.adj = [[] for _ in range(len(nodes))]  # adjacency list
        self.nodes = nodes  # list of nodes

    def graph_add_edge(self, edge):
        """
        Add an edge to the graph.

        Args:
            edge (Edge): The edge to add.
        """
        self.adj[edge.source].append(RES_EDGE(edge.source, edge.target, edge.capacity))
        self.adj[edge.target].append(RES_EDGE(edge.target, edge.source, 0))  # Reverse edge with 0 capacity

    def bfs(self, source, sink, parent):
        """
        Perform BFS to find an augmenting path in the residual graph.

        Args:
            source (int): The source node.
            sink (int): The sink node.
            parent (list): To store the path.

        Returns:
            bool: True if an augmenting path is found, False otherwise.
        """
        visited = [False] * len(self.adj)
        queue = deque([source])
        visited[source] = True

        while queue:
            current = queue.popleft()

            for edge in self.adj[current]:
                if not visited[edge.target] and edge.capacity - edge.flow > 0:  # Check for residual capacity
                    queue.append(edge.target)
                    visited[edge.target] = True
                    parent[edge.target] = edge
                    if edge.target == sink:
                        return True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [None] * len(self.adj)
        max_flow = 0

        # Augment the flow while there is a path from source to sink
        while self.bfs(source, sink, parent):
            # Find the bottleneck capacity (minimum residual capacity along the path)
            path_flow = float('Inf')
            current = sink
            while current != source:
                edge = parent[current]
                path_flow = min(path_flow, edge.capacity - edge.flow)
                current = edge.source

            # Update the flow along the path
            current = sink
            while current != source:
                edge = parent[current]
                edge.flow += path_flow
                # Find the reverse edge and update its flow
                for rev_edge in self.adj[edge.target]:
                    if rev_edge.target == edge.source:
                        rev_edge.flow -= path_flow
                        break
                current = edge.source

            max_flow += path_flow

        return max_flow
    """
        # Placeholder for implementation
        print("test")
        pass
        #approach: residual network
        #start from 0 flow
        current_flow = 0
        while True:
            if current_flow == max():#flow has reached max capacity from source
                break

        #bfs
        
        
    current_flow = min(path_capacity)
    for i in path:
          #  update flow of all edges to current_flow
        #augment path
        #if can't augment anymore, stop
    #        return max_flow
    """

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