# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # This is the base case
        # not root: we've hit an empty brancj, so there's nothing here to report
        # root.val == p.val: we've found value of p itself, return this node
        # root.val == q.val: we've found value of q itself, return this node
        if not root or root.val == p.val or root.val == q.val:
            return root
        # Recursively search the left and right subtrees for p and q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # If both left and right return non-None, that means p is on one side and q is on the other side. Since p and q live in different branches of root, root is the LCA
        if left and right:
            return root
        # If we get here, it means at most one side found anything. Either only left is non-None or only right is non-None
        return left if left else right