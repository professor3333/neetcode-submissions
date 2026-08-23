# Defines the blueprint for a single node in our Trie
class TrieNode:
    # The constructor that initializes a new node
    def __init__(self):
        # A dictionary that maps a character to another TrieNode. This represents the edges connecting to the next character. 
        self.children = {}
        # A boolean flag: It is False by default. It becomes True only when this specific node marks the end of a valid, inserted word
        self.is_end = False

class PrefixTree:
    # Constructor for the Trie
    def __init__(self):
        # Initializes the Trie with an empty root node. The root itself doesn't hold a character; it's just the starting point
        self.root = TrieNode()

    # Takes a string word and adds it to the trie
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        
        
        