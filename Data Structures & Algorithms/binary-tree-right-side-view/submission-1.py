# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            # Runs a loop exactly level_size times. This uses an explicit index i because we need to know which iteration we're on, to detect the last one
            for i in range(level_size):
                node = queue.popleft()
                # Since nodes within a level are always processed in left-to-right order, the last ndoe processed in this level's loop(i = level_size - 1) must be the rightmost node at this level
                if i == level_size - 1:
                    result.append(node.val)
                # Push this node;s children onto the queue for processing in the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result