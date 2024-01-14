# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        # Base case: If root1 is None, return root2
        if root1 is None:
            return root2

        # Base case: If root2 is None, return root1
        if root2 is None:
            return root1

        # Merge the values of the current nodes
        root1.val += root2.val

        # Recursively merge the left and right subtrees
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
