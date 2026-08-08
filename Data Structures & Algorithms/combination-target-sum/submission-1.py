class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current_combination, current_sum):
            if current_sum == target:
                result.append(current_combination.copy())
                return
            
            if current_sum > target or i >= len(nums):
                return

            current_combination.append(nums[i])
            dfs(i, current_combination, current_sum + nums[i])

            current_combination.pop()

            dfs(i + 1, current_combination, current_sum)

        dfs(0, [], 0)
        return result