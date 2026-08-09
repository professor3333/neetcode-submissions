class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort() # This sorts the candidates list in increasing order
        res = [] # Creates and empty list called res which will store all valid combinations whose sum equals target

        # This defines a helper function called backtrack. This function performs the recursive search
        def backtrack(start, path, remaining):
            # This checks whether we have reached the target exactly
            if remaining == 0:
                # If the current path is valid, we add a copy of it to res, because path is a list that will keep changing during backtracking
                res.append(path.copy())
                return
            # This starts a loop from the start index to the end of candidates
            for i in range(start, len(candidates)):
                # Pruning: Because candidates is sorted, if the current candidate is greater than remaining, then all later candidates are also greater than remaining
                if candidates[i] > remaining:
                    break
                # This line prevents duplicate combinations. If this candidate is the same as the previous candidate, and we are at the same recursion level, skip it
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # We choose the current candidate. We add it to path
                path.append(candidates[i])
                # Move to the next index(i + 1) because each number can only be used once. We also do remaining - candidates[i] because we just added candidates[i] to the combination
                backtrack(i + 1, path, remaining - candidates[i])
                # This is the backtracking step. This removes the last number from path. After exploring the branch where we chose candidates[i], we undo that choice so we can try other candidates
                path.pop()
        # This starts the backtracking process
        backtrack(0, [], target)
        return res # res contains all unique valid combinations