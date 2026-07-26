# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # A node is good if its value is >= maximum value seen so far
            is_good = 1 if node.val >= max_val else 0
            
            # Update the max value seen on this path
            max_val = max(max_val, node.val)
            
            # Recurse left and right
            left_count = dfs(node.left, max_val)
            right_count = dfs(node.right, max_val)
            
            return is_good + left_count + right_count

        # Start DFS with the root value as the initial max value
        return dfs(root, root.val)