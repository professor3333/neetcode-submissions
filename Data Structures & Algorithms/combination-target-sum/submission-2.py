class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] # This creates an empty list which will store all valid combinator
        # This defines a helper function called dfs. This function explores possible combinations recursively. i is the current index in nums. current_combination is the combination we are currently building. current_sum is the sum of the number in current_combination
        def dfs(i, current_combination, current_sum):
            # This checks whether the current combination already equals the target. 
            if current_sum == target:
                # We add it to res. We use .copy() because lists in python are mutable. That means current_combination will keep changing as we continue backtracking. 
                result.append(current_combination.copy())
                return # After finding a valid combination, we stop exploring this branch
            # If the current sum is > target, or, whether we have gone past the last candidate, there is no point continuing
            if current_sum > target or i >= len(nums):
                return
            # Decision 1) We add candidates[i] to the current combination
            current_combination.append(nums[i])
            # Now we recursively continue searching
            dfs(i, current_combination, current_sum + nums[i])
            # This is the backtracking step. After exploring the branch where we included candidates[i], we remove it from current_combination. This allows us to try other possibilities 
            current_combination.pop()
            # Decision 2) Exclude the current candidate and move to the next one. We pass (i + 1) because we are done conisdering candidates[i] for this branch 
            dfs(i + 1, current_combination, current_sum)
        # This starts the recursive search. We begin with i = 0, current_comb = [], and current_sum = 0
        dfs(0, [], 0)
        return result # result contains all valid combinations