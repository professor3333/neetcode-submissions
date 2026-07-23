# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subRoot is always a subtree
        if not subRoot:
            return True
        # If root is empty but subroot isn't, it can't be a subtree
        if not root:
            return False
        # If the entire tree rooted at root exactly math subRoot, we have found our match, return True immediately
        if self.isSameTree(root, subRoot):
            return True
        # Otherwise, recursively search the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)