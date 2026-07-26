# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs returns the count of good nodes found within the subtree rooted at node
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            # A node is good if its value is >= max_val seen so far 
            is_good = 1 if node.val >= max_val else 0
            # Update the running maximum to include this node's own value, before recursing into its children
            max_val = max(max_val, node.val)
            # Recurse into the left and right subtrees, passing along the updated max_val(which now includes the current node), so each child correctly knows the true maximum along its own path from the root
            left_count = dfs(node.left, max_val)
            right_count = dfs(node.right, max_val)

            return is_good + left_count + right_count
        # Kick off the recursion starting at the root, with max_val initialized to root.val itself, since the root's own value is the maximum seen so far
        return dfs(root, root.val)
