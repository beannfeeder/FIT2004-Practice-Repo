class Node:
    """
    self.data - stores the data 
    self.links - list of None with the len(total of keys and terminal char) - e.g. len() = 27 from 1 terminal char $ and 26 alphabet char
                e.g. [$, a, b, c, d...]
    """
    def __init__(self, data=None):
        self.data = data
        self.links = [None]*27

class Trie:
    """
    init - just the root

    insert - 

    search 

    """
    def __init__(self):
        self.root = Node()
    
    def insert(self, key, data):
        """
        iterative implementation
        """
        for char in key:
            print(char)
            
    
    def search(self):
        pass

#example
the_strings = [["apple", 1024],["app", 64],["appendix",234],["lol", 69]]

example_trie = Trie()
for pair in the_strings:
    example_trie.insert(pair[0],pair[1])

