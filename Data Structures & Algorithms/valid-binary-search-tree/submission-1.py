# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # validate checks whether the subtree rooted at node is a valid BST, given that every value in this subtree is required to fall strictly between min_val and max_val
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True
            # If the current node's value doesn't strictly fall within its allowed range, the BST property is violated right here, return False immediately
            if not (min_val < node.val < max_val):
                return False
            # If the current node passed the above check, we now recures it's children. left subtree must be < node.val, right subtree must be > node.val. Both subtree must return True for the overall subtree to be valid
            return(validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val))

        # Kick off the recursion at the root with no constraints at all. Start with infinite bounds(-infinity to infinity)
        return validate(root, float('-inf'), float('inf'))