class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [] # The global list that will store all the final subsets we find 
        subset = [] # A working list that stores the subset we are currently building as we traverse the decison tree
        def dfs(i): 
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res