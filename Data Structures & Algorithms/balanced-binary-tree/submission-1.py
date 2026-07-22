# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs computes and returns the height of the subtree rooted at node
        def dfs(node) -> int:
            if not node:
                return 0

            # Recursively compute the height of the left subtree
            left_height = dfs(node.left)
            if left_height == -1:
                return -1 # Left subtree is already unbalanced

            # # Recursively compute the height of the right subtree
            right_height = dfs(node.right)
            if right_height == -1:
                return -1 # Right subtree is already unbalanced
            
            # If the absolute value of difference between left and right subtree heights exceeds 1, this node makes the tree unbalanced, so return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of the current node
            return 1 + max(left_height, right_height)

        # If dfs(root) returns anything other than -1, the tree is balanced
        return dfs(root) != -1