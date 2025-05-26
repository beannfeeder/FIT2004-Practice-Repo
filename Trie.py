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
        current = self.root
        for char in key:
            #print(char)
            actual_key = ord(char) - 97 + 1 #97 for starting small alphabet, 1 for leaving space for terminal char
            if current.links[actual_key]: #there is a path, move current to that path
                current = current.links[actual_key]

            else: #no path, create one out and move current
                #print("making new node")
                current.links[actual_key] = Node()
                current = current.links[actual_key]
        #finished adding char nodes, now end with terminal char $
        # we know we left out node.links[0] as the terminal char section
        terminal_key = 0
        if current.links[terminal_key]: # there is a previous version of the word, we are just updating the data
           # print("magic!")
            current = current.links[terminal_key]
            
        else: #make a end node
            current.links[terminal_key]=Node()
            current = current.links[terminal_key]

        current.data = data
        #print(data)
    
    def search(self, key):
        """
        traverse through nodes and return the data of the given input key
        """
        current = self.root
        for char in key:
            print(f"searching {char}")
            actual_key = ord(char) - 97 + 1 #97 for starting small alphabet, 1 for leaving space for terminal char
            if current.links[actual_key]: #there is a path, move current to that path
                current = current.links[actual_key]

            else: #no path, create one out and move current
                raise Exception(f"key {char} not in trie")
        terminal_key = 0
        if current.links[terminal_key]:
            current = current.links[terminal_key]
            return current.data
        else:
            raise(KeyError, "some other error lol")



#example
the_strings = [["apple", 1024],["app", 64],["appendix",234],["lol", 69], ["apple",6789]]

example_trie = Trie()
for pair in the_strings:
    example_trie.insert(pair[0],pair[1])
try:
    print(example_trie.search("apple"))
except Exception as e:
    print(e)
try:
    print(example_trie.search("pie"))
except Exception as e:
    print(e)
