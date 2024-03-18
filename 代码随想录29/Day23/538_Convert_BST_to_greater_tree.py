# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Initialize a variable to store the sum of greater values
        self.pre = 0
        # Start the traversal from the root
        self.traversal(root)
        return root

    def traversal(self, cur):
        # Base case: if the current node is None, return
        if cur is None:
            return
        # Traverse the right subtree
        self.traversal(cur.right)
        # Update the current node's value by adding the sum of greater values
        cur.val += self.pre
        # Update the sum of greater values with the updated current node's value
        self.pre = cur.val
        # Traverse the left subtree
        self.traversal(cur.left)
