# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        # dfs is a helper function that computes the height of the subtree rooted at node, while also updating max_diameter
        def dfs(node):
            # Tells python to modify the max_diameter variable defined in the outer parent function rather than creating a new local variable
            nonlocal max_diameter

            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_diameter = max(max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diameter