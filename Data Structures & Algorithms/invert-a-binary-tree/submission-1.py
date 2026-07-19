# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Using deque for efficient O(1) pops from the front
        # This queue will hold nodes we still need to process, nodes whose children haven't been swapped yet
        queue = deque([root])

        # Keep processing as long as there are nodes left in the queue
        while queue:
            # Pop the front node from the queue. Every node gets visited from left to right processing order
            current = queue.popleft()

            # Swap children
            current.left, current.right = current.right, current.left

            # After swapping, add the node's children to the queue, so they'll have their own children swapped too
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        # The inversion is done in place, mutating the original tree rather than building a new one
        return root