# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A base case is the conditional hook in a recursive function that stops the recursion from executing infinitely
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: If both nodes are None, that means both trees ended here simultaneously
        if not p and not q:
            return True

        # Base case 2: One node is None or values don't match. (p.val != q.val): both nodes exist but they hold different values
        # Any one of them being true causes an immediate False. Here False is returned if the function is true
        if not p or not q or p.val != q.val:
            return False

        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)