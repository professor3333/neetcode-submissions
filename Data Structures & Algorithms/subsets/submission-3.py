class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] # The global list that will store all the final subsets we find
        subset = [] # A working list that stores the subset we are currently building as we traverse the decision tree

        # This represents the index of the element in nums that we are currently making a decision about
        def dfs(i):
            # Once i has gone past the end of nums, that means we've made an include/exclude decision for every element
            if i >= len(nums):
                # We must use .copy() because in Python, lists are objects. If we appended the original subset list, every entry in res would point to the same list, and as we pop() later, those entries would end up empty
                result.append(subset.copy())
                return
            
            # Decision 1) We add nums[i] to our current working subset. 
            subset.append(nums[i])
            # We call dfs(i + 1) to move to the next index, carrying this number with us
            dfs(i + 1)
            
            # Decision 2) This is the backtracking step. We remove nums[i] which is the element we just added, to revert the state back to how it was before the include decision
            subset.pop()
            # We call the function again for the next index, but this time the current number is not in the subset
            dfs(i + 1)

        # Kick off the recursion starting at index 0, and once the entire recursion process completes, res contains all 2^n subsets
        dfs(0)
        return result