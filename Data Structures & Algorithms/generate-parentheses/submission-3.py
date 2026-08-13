class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] # store all valid parenthese combinations
        path = [] # stores the current sequence of parentheses being built

        # This function recursively build parentheses strings 
        def backtrack(open_count, close_count):
            # It checks whether we have used exactly n opening, and exactly n closing parentheses, then one full valid combination is complete
            if open_count == n and close_count == n:
                # If the combination is complete, we join the list path into a string and add it to res
                res.append("".join(path))
                return

            # We can add "(" as long as we have not used all n opening parentheses yet
            if open_count < n:
                path.append("(") # We add an opening parentheses 
                # We increase open_count by 1 because we just added an opening parentheses
                backtrack(open_count + 1, close_count) 
                # After the recursive call finishes, we remove the last parentheses from path
                path.pop()

            # We can add ")" only if there are fewer closing parantheses than opening parentheses currently in the path
            if close_count < open_count:
                path.append(")") # We add a closing parentheses
                backtrack(open_count, close_count + 1) # Increase close_count by 1
                path.pop() # After the recursive call finishes, we remove the closing parentheses to try other possibilites

        backtrack(0, 0) # THis starts the backtrackign process
        return res # Contains all valid parentheses combinations