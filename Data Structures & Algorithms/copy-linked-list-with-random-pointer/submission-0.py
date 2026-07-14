"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_clone = {None: None}

        curr = head
        while curr:
            clone = Node(curr.val)
            old_to_clone[curr] = clone
            curr = curr.next

        curr = head
        while curr:
            clone_node = old_to_clone[curr]
            clone_node.next = old_to_clone[curr.next]
            clone_node.random = old_to_clone[curr.random]
            curr = curr.next
        
        return old_to_clone[head]