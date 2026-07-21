# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        # dfs is a recursive function that visits a specific node, calculates the height of its left and right subtrees, and then moves down to its children
        def dfs(node):
            # This keyword allows the inner dfs function to modify a variable named max_diameter that lives outside of it (in the parent function), rather than creating a new variable
            nonlocal max_diameter

            if not node:
                return 0

            # Recursively find the height of the left and right subtress. This is a post-order traversal
            left_height = dfs(node.left) # Goes down the left side of the tree to find its total height
            right_height = dfs(node.right) # Goes down the right side of the tree to find its total height

            # (left_height + right_height) is the length(number of edges) that passes through the current node, going down to it's left subtree and down to it's right subtree
            # This checks every single node as a potential "peak" of the longest path, not just the root, which is exactly what's needed since the true diameter could be buried entirely inside a subtree.
            max_diameter = max(max_diameter, left_height + right_height)

            # Calculates the total height or depth of a node in a binary tree by adding 1(for the current node) to the larger height between its left and right subtrees
            return 1 + max(left_height, right_height)
        
        # dfs(root) is a recursive helper function call that returns the maximum height of the binary tree. Kick off the recursion from the root. Once it completes, every node in the tree has had its "diameter through this node" checked and compared, so max_diameter holds the true answer -> the longest path anywhere in the tree
        dfs(root)
        return max_diameter
