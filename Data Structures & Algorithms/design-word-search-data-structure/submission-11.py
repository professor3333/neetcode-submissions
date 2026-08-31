# We define our TrieNode
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

# We initialize our WordDictionary with an empty root node
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    # We iteratively traverse the Trie, creating new nodes for characters that don't exist yet, and finally mark the end of the word with is_end = True
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
    # Searching for a Word (The Core Logic)
    def search(self, word: str) -> bool:
        # We define a nested helper function using Depth-First Search. It takes the current character index we are looking at in the word, and the node we are currently at in the Trie.
        def dfs(index: int, node: TrieNode) -> bool:
            # Set our current pointer to the passed-in node.
            curr = node
            # Loop through the characters of the word starting from the given index.
            for i in range(index, len(word)):
                # Get the current character.
                char = word[i]
                
                # Wildcard case: try all possible matching paths
                if char == ".": # If the character is a dot, it can be any letter.
                    # We iterate through all available child nodes (the actual TrieNode objects) connected to our curr node.
                    for child in curr.children.values():
                        # For each child, we recursively call dfs, moving to the next character index (i + 1) and passing the child node.
                        if dfs(i + 1, child):
                            # If any of those recursive calls eventually finds a valid word, we immediately return True
                            return True
                    # If we exhaust all children and none of them lead to a valid word, this path is a dead end. Return False.
                    return False
                
                # Standard character lookup
                # If it's a normal letter and the path doesn't exist, the word isn't in the dictionary.
                if char not in curr.children:
                    # Return False immediately.
                    return False
                # Move down the Trie to the matching child node.
                curr = curr.children[char]
            # If the loop finishes without hitting a return False, we've matched all characters. We return whether this final node marks the end of a valid word.
            return curr.is_end
        # Kick off the recursion starting at index 0 and the root node.
        return dfs(0, self.root)