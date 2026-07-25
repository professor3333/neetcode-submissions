# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: an empty tree has no levels at all
        if not root:
            return []
        # result will be the final list-of-lists
        result = []
        # queue contains a single element root node to start the BFS
        queue = deque([root])
        # runs as long as a queue data structure contains items
        while queue:
            # level_size records how many nodes exist in the current depth. current_level will collect this level's values
            level_size = len(queue)
            current_level = []
            # Process exactly level_size nodes
            for _ in range(level_size):
                # Pop the next node from the front of the queue
                node = queue.popleft()
                # Record its .val into current_level
                current_level.append(node.val)
                # Push it's children onto the back of the queue, these belong to the next level and will be processed in the next iteration of the outer while loop
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Once all level_size nodes for this level have been processed, current_level now holds the complete, correctly ordered list of values for this level
            result.append(current_level)
        return result