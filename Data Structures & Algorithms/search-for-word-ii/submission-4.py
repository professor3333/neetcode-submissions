class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Store complete word at the leaf node

        ROWS, COLS = len(board), len(board[0])
        result = []

        # Step 2: DFS Traversal with pruning
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # Check if we matched a word
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Avoid adding duplicates

            # Mark cell as visited in-place
            board[r][c] = '#'

            # Explore 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Backtrack to original state
            board[r][c] = char

            # Optimization: Remove leaf nodes with no remaining children
            if not curr_node.children:
                parent_node.children.pop(char)

        # Step 3: Start search from every cell matching root children
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result