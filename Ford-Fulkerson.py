
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
        #find augmenting path, if no edges starting from the source leads to the sink, no augmenting path found
            for edge in self.adj[current]:
                #forward edge: residual capacity > 0
                if not visited[edge.target] and edge.capacity - edge.flow > 0:  # Check for residual capacity
                    queue.append(edge.target)
                    visited[edge.target] = True
                    parent[edge.target] = edge
                    if edge.target == sink:
                        return True

        #no augmenting path found, return false to terminate the BFS
        return False

    def ford_fulkerson(self, source, sink):
        """
        Approach:
        Start from 0 flow
        while loop bfs to check for augmenting path
            current_flow = min(capacity of all edges)
            update flow of all edges to current_flow
            loop back

        if can't augment anymore, stop

        return max_flow
        """
        parent = [None] * len(self.adj)
        max_flow = 0

        # Augment the flow while there is a path from source to sink
        while self.bfs(source, sink, parent):
            # start from the sink node
            path_flow = float('Inf')
            current = sink
            while current != source:
                edge = parent[current]
                path_flow = min(path_flow, edge.capacity - edge.flow) # updating the flow to the minumum
                current = edge.source #backtrack

            # Update the flow along the path
            current = sink
            while current != source:
                edge = parent[current]
                edge.flow += path_flow
                edge.capacity -= path_flow

                # Find the reverse edge and update its flow
                for rev_edge in self.adj[edge.target]:
                    if rev_edge.target == edge.source: #unsure
                        rev_edge.capacity += path_flow
                        rev_edge.flow -= path_flow
                        break
                current = edge.source

            max_flow += path_flow
        
        return max_flow


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



"""
Simple question:
     2         
  A --- C---  
 /2         \ 2
S            F       it should be 2 + 1, SACF can hold 2, SBDF can hold 1 returns a maxflow of 3
 \ 3   1     /
   \- B----D/ 3
"""

# Define nodes and edges
nodes = [0, 1, 2, 3, 4, 5]
edges = [
    Edge(0, 1, 2),  # S -> A with capacity 2
    Edge(0, 2, 3),  # S -> B with capacity 3
    Edge(1, 3, 2),  # A -> C with capacity 2
    Edge(2, 4, 1),  # B -> D with capacity 1
    Edge(3, 5, 2),  # C -> F with capacity 2
    Edge(4, 5, 3)   # D -> F with capacity 3
]

# Create the graph
graph = Graph(nodes)
for edge in edges:
    graph.graph_add_edge(edge)

banana = []*5
print(banana)
print("lol")
# Find the maximum flow
source = 0  # S
sink = 5    # F
for node in graph.adj:
    for edge in node:
        print(edge.capacity)
print("BEFORE")
print("apple")
max_flow = graph.ford_fulkerson(source, sink)

print(f"Maximum Flow: {max_flow}")


"""
Feedback from Dr. Ian:
1. To avoid confusion, RES_EDGE should just have one attribute for weight. No need to have self.flow in line-139 and this maks the whole line-44 complex. On the other hand, the Edge class as per line-120 should have both flow and capacity attributes.
2. Think you want to reset parent at the end of each iteration? For example after line-95. It is fine for now but no harm resetting it.
3. You shouldn't need the loop in line-88 if you follow what I said in class about forward edge storign reference to backward edge and vice versa. Thus you line-13 graph_add_edge() needs to be udpated.
4. The whole update in block-89 is wrong. Logic for updating the augmented edge seems off for the entire block. Consider the following logic:
        If augmenting a forward edge:
            the forward edge weight -bottleneck.
            the backward edge weight +bottleneck.
            the flow edge +bottleneck.
        If augmenting a backward edge:
            the backward edge weight -bottleneck.
            the forward edge weight +bottleneck.
            the flow edge -bottleneck.

"""