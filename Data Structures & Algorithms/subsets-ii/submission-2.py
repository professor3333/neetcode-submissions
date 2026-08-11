class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sorts nums in increasing order. SOrting places duplicate values next to each other
        nums.sort()
        res = []
        # start tells us which index we are allowed to consider next. This prevents the algorithm from going backward and creating duplicate or repeated subsets. path is the subset currently being built
        def backtrack(start, path):
            # Record current subset at every step
            res.append(path.copy())
            # This loops through the candidates starting from index start
            for i in range(start, len(nums)):
                # This is the duplicate skipping logic
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # We choose the current number. We add it to current subset
                path.append(nums[i])
                # Now we recursively continue building subsets
                backtrack(i + 1, path)
                # This is the backtracking process. After the recursive call finishes, we remove the numbers we just added
                path.pop()
        backtrack(0, []) # This starts the backtracking process
        return res # res contains all unique subsets