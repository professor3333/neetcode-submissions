# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The most optimal approach is an in-order traversal(left, root, right) processes the node in sorted, ascending order

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stack will hold nodes we've visited
        stack = []
        # curr is a pointer used to walk down the tree
        curr = root

        # Keep going as long as there's either more tree to explore or unprocessed ancestors waiting on the stack
        while stack or curr:
            # This inner loop walks all the way down the left spine of the current subtree, pushing every node visited along the way onto the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            # Once we can't go left anymore, pop the most recently pushed node off the stack, this is the next node in-order sequence
            curr = stack.pop()
            # Decrement k, since we've now visited one more node in sorted order
            k -= 1
            # If k is 0, we've just visited exactly the k-th smallest node, so return it's value immediately
            if k == 0:
                return curr.val
            # If we haven't found the k-th element yet, move to this node's right subtree next. This is the in-order traversal's natural next step: after processing a node, we must process its right subtree before returing to any remaining ancestor on the stack
            curr = curr.right
        
        return -1