# The optimal solution for the N-Queens problem uses Backtracking (DFS) with Hash Sets for $O(1) constraint checking.
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Creates an epmty set called cols, stores the columns that already have a queen 
        cols = set()
        # Stores one type of diagonal. Identified by r + c
        posDiag = set()
        # Stores the other type of diagonal. Identified by r - c
        negDiag = set()
        # res will store all valid board configurations
        res = []
        # This creates the chessboard. It is an n x n grid filled with dots. 
        board = [["."] * n for _ in range(n)]
        # It recursively tries to place queens row by row. r is the current row where we are trying to place a queen
        def backtrack(r: int):
            # Base case) It checks whether we have placed queens on all rows. if r == n, then every row has a queen
            if r == n:
                # If we placed queens on all rows, we add the current board to res. This converts the board from a list of lists into a list of strings
                res.append(["".join(row) for row in board])
                return
            # This loops through every column in the current row. Since we place one queen per row, we need to try every possible column in row r
            for c in range(n):
                # This checks whether placing a queen at (r,c) would conflict with any previously placed queen
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    # If any conflict exists, we skip this column and try the next one
                    continue

                # If there's no conflict, we place a queen. First we mark column c as occupied
                cols.add(c)
                # We mark the r + c diagonal as occupied. Now, no future queen can be placed on that diagonal. 
                posDiag.add(r + c)
                # We mark the r - c diagonal as occupied. Now, no future queen can be placed on that diagonal. 
                negDiag.add(r - c)
                # We visually place the queen on the board
                board[r][c] = "Q"

                # Now that we place a queen in row r, we move to the next row
                backtrack(r + 1)

                # After the recursive call returns, we backtrack. First, we remove the column from cols. This marks the column as available again
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res
