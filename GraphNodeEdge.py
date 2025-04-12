## Graph class for BFS and DFS: Weighted
class Graph:
    def __init__(self, arr):
        # arr = list of nodes
        self.nodes = [None] * len(arr)
        for i in range(len(arr)):
            self.nodes[i] = Node(arr[i])
    
    def __str__(self):
        # Returns the string representation of the graph
        return_str = ""
        for node in self.nodes:
            return_str = return_str +"Node "+ str(node)+"\n"
        return return_str
    
    
    def BFS(self, source_node):
        # BFS traversal of the graph
        # BFS, uses queue, go wide first
        # basic, try to improve

        return_bfs = []
        discovered = [] # try to improve and use actual queue instead of list
        discovered.append(source_node)
        source_node.visited = True
        while len(discovered) > 0:
            x= discovered.pop(0) # x is the current node in the BFS
            x.visited = True
            return_bfs.append(x)
            for edge in x.edges:
                y = edge.y
                if y.discovered == False:
                    discovered.append(y)
                    y.visited = True # mark y as discovered
        return return_bfs
    
    def DFS(self, source_node):
        # DFS traversal of the graph
        # DFS, uses stack, go deep first
        # basic, try to improve
        return_dfs = []
        discovered = [] # discovered is a stack, LIFO
        discovered.append(source_node)  
        source_node.visited = True
        while len(discovered) > 0:
            x= discovered.pop(0) # x is the current node in the BFS
            x.visited = True
            return_dfs.append(x)
            for edge in x.edges:
                y = edge.y
                if y.discovered == False:
                    discovered.append(y)
                    y.visited = True # mark y as discovered
        return return_dfs
class Node:
    def __init__(self, id):
        # id = id of the node, edges = list of edges connected to the node
        self.id = id
        self.edges = []
        self.visited = False

    def add_edge(self, target_node, weight):
        # Adds an edge to the node
        edge = Edge(self, target_node, weight)
        self.edges.append(edge)

    def __str__(self):
        # Returns the string representation of the node
        return_str = str(self.id)
        return return_str
       
class Edge:
    def __init__(self, x, y, w):
        # x = node 1, y = node 2, w = weight
        self.x = x
        self.y = y
        self.w = w


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 4, 5]
    g = Graph(arr)
    #print(g) # Output: 1,2,3,4,5
    g.nodes[0].add_edge(g.nodes[1], 1)
    g.nodes[0].add_edge(g.nodes[4], 2)
    g.nodes[1].add_edge(g.nodes[2], 3)
    g.nodes[2].add_edge(g.nodes[3], 4)
    g.nodes[3].add_edge(g.nodes[4], 5)
    print(g.BFS(g.nodes[0]))
