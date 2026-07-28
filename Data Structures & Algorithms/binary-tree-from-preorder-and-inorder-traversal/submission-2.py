# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # precompute a dictionary mapping each value to its index in the inorder list. This lets us find "where does this root value split the inorder sequence?"
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        # This tracks our current position in the preorder list
        pre_idx = 0

        # array_to_tree(left, right) builds and returns the subtree whose nodes occupy the inorder index range[left, right]. The nonlocal pre_idx lets this inner function modify the shared pre_idx counter, so progress through preorder is tracked consistently across all recursive calls
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            # If the range is empty, there's no subtree here, return None
            if left > right:
                return None
            
            # The current preorder element is the root of this subtree. Grab that value, create a new Tree Node for it, and advance pre_idx so the next recursive call picks up the next preorder element
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Now that we know the root's value, look up where this root sits within the inorder sequence. This index is tne crucial "splitting point": everything to its left in inorder belongs to the left subtree, everything to its right belongs to the right subtree
            inorder_idx = inorder_map[root_val]

            # Recursively build the left subtree, using the inorder range from the original left boundary up to the root's position
            root.left = array_to_tree(left, inorder_idx - 1)
            # Recursively build the right subtree, using the inorder range just after the root's position up to the original right boundary
            root.right = array_to_tree(inorder_idx + 1, right)
            # Return the fully constructed subtree rooted at root with .left and .right
            return root
        # kick off construction using the entire inorder range, since the whole tree corresponds to all of inorder's indices from 0 to len(inorder) - 1
        return array_to_tree(0, len(inorder) - 1)