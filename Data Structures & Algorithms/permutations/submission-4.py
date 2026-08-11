class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [] # Stores the current permutation being built
        used = set() # Empty set which keeps track of which numbers have already been used in the current path
        
        # Defines a helper function called backtrack. This function recursively builds permutations. It does not need parameters because it can access: nums, res, path, used from the outer function
        def backtrack():
            # Base case: completed a full permutation. Add it to res, add path.copy() because path is a mutable list that will keep changing during backtracking
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            # This loops through every number in nums. At each step, we try placing num into current permutation
            for num in nums:
                # Checks whether num has already been used in the current permutation
                if num in used:
                    continue # If already used, skip it, and continue to next number
                
                # .add() is exclusively used to insert items into a set, while  is exclusively used to add items to the end of a list.
                # Choose step) If num has not been used yet, we add it to used. This marks num as used
                used.add(num)
                path.append(num) # We also add num to the current permutation

                # Explore step) Now we call backtrack() recursively. This continues building the permutation using the current choices
                backtrack()

                # Unchoose step) After the recursive call finishes, we remove the last number from path
                path.pop()
                used.remove(num) # We also remove num from used. This marks num as unused again

        backtrack() # This starts the backtracking process
        return res # res contains all complete permutations