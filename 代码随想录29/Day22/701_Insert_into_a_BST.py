# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Helper function for recursive traversal and insertion
        def traversal(root, val):
            # If the current node is None, create a new node with the given value
            if root is None:
                node = TreeNode(val)
                return node

            # If the value to be inserted is less than the current root value,
            # insert it into the left subtree
            if val < root.val:
                root.left = traversal(root.left, val)
            # If the value to be inserted is greater than the current root value,
            # insert it into the right subtree
            elif val > root.val:
                root.right = traversal(root.right, val)

            return root

        # Start traversal from the root
        return traversal(root, val)
