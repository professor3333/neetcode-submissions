# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # This is a straightforward preorder DFS (node -> left -> right)
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        # If node is none, append "N" to mark there's nothing here, this is what gives deserialize enough information to know exactly where each subtree end
        def dfs(node):
            if not node:
                vals.append("N")
                return
            # Otherwise, append the node's value as a string, since we're building a single string overall, then recurse left, then recurse right
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        # Finally, join all the collected tokens with commas into one string
        dfs(root)
        return ",".join(vals)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the comma separated string back into a list of tokens, then wrap it in an iterator
        vals = data.split(",")
        # Take that list and turn it into an iterator, which lets you get th next item using next()
        vals_iter = iter(vals)

        def dfs():
            # Fetches the next token from an iterator of split string values
            val = next(vals_iter)
            if val == "N":
                return None
            # If this token represents a real node value, create a TreeNode from it, then recursively call dfs() to build its left child first, then its right child
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            # Finally, it reutrns the constructed node back upto its parebt
            return node

        # Kick off the recursion by calling dfs() once for the whole tree, this single call will recursively consume every token in vals_iter, building the complete tree before reurning
        return dfs()
