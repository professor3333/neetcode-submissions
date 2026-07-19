# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Initialize the queue with just the root node
        queue = deque([root])
        depth = 0

        # Keep going as long as there are still nodes left to process at some level
        while queue:
            # Root node counts as one level of depth
            depth += 1
            # Before we start popping, we record how many nodes currently belong to this level. At the start of each iteration of the while loop, the queue contains only the nodes of the current level
            level_size = len(queue)

            # This inner loop processes exactly level_size nodes: exactly the nodes that were in the queue at the start of this level
            for _ in range(level_size):
                # Pop it from the front
                node = queue.popleft()
                # Checks if a left child exists and add it to the back of the queue
                if node.left:
                    queue.append(node.left)
                # Checks if a right child exists and adds it to the back of the queue
                if node.right:
                    queue.append(node.right)

        # Once the queue is completely empty, depth holds the total number of level or the max depth of the tree
        return depth