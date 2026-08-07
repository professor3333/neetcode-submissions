class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, comb, sum):
            if sum == target:
                res.append(comb.copy())
                return

            if sum > target or i >= len(nums):
                return

            comb.append(nums[i])
            dfs(i, comb, sum + nums[i])

            comb.pop()

            dfs(i + 1, comb, sum)

        dfs(0, [], 0)
        return res