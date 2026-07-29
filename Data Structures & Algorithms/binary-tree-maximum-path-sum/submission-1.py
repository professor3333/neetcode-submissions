# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def get_max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Max gain from left and right subtrees; ignore negative contributions  
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            # Sum of the path passing through the current node as the peak
            current_path_sum = node.val + left_gain + right_gain
            # Update the global maximum path sum
            max_sum = max(max_sum, current_path_sum)
            # Return max single branch gain to extend to the parent node
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return max_sum