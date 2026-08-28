class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, parent, char):
            curr = parent.children[char]

            if curr.word:
                res.append(curr.word)
                curr.word = None

            board[r][c] = "#"

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    next_char = board[nr][nc]
                    if next_char in curr.children:
                        dfs(nr, nc, curr, next_char)
            board[r][c] = char
            if not curr.children:
                parent.children.pop(char)

        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                if char in root.children:
                    dfs(r, c, root, char)

        return res