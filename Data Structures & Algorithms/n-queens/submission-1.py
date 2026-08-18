class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int):
            # Base case: placed queens on all n rows
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                # Check for conflicts
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                # Place queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                # Recurse to next row
                backtrack(r + 1)
                # Backtrack (remove queen)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res