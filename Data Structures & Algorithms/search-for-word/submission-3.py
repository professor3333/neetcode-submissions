class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # This calculates the number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])
        # r: current row index, c: current column index, index tells us which character in word we are currently trying to match
        def dfs(r, c, index):
            # Base case: If index equals the length of word, it means we have successfully matched every character
            if index == len(word):
                return True
            # Row is too small, means we moved above the top row of the board or Row is too large, means we moved below the bottom row or 
            # Column is too small, means we moved too far left or Column is too large, means we moved too far right or
            # Character mismatch, means the current board cell does not contain the character we need next. If any of this condition is true, we return False
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[index]):
                return False
            # This saves the current board character in a temporary variable. We save it because we are about to temporarily modify the board
            temp = board[r][c]
            # This marks the current cell as visited. We temporarily change the character to something that cannot appear in word. Since the same letter cell may not be used more than once, marking the cell as visited is necessaru
            board[r][c] = "#"
            # Explore all four possible directions from the current cell. Each reucrsive call tries to match the next character of the word. We pass: index + 1 because we have successfully matched the current character: word[index]. Now we need to match the next character: word[index + 1]. 
            # If any one of these directions leads to a complete match, the result is True
            found = (dfs(r + 1, c, index + 1) or # Down
                     dfs(r - 1, c, index + 1) or # Up
                     dfs(r, c + 1, index + 1) or # Right
                     dfs(r, c - 1, index + 1))   # Left
            # Backtracking step) This restores the original character in the board. This is important because other search paths may need to use this cell later. We only want to mark the cell as visited during the current path, not permanently
            board[r][c] = temp
            # This returns whether a valid path was found starting from the current cell. If one of the four directions eventually matched the entire word, found is True
            return found
        # These nested loops visit every cell in the board. The word can start anywhere in the grid. So we try starting the DFS from each cell 
        for r in range(ROWS):
            for c in range(COLS):
                # For each cell, we first check whether it matches the first character of the word. This is an optimization. If the current cell does not match the first character, there is no reason to start a DFS from it. If it does match, we call: dfs(r, c, 0). We pass index = 0, because we are trying to match the first character. If dfs returns True, then the full word exists in the board. So we immediately return: True
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        # If we try every cell and none of them can build the word, we return: False
        return False