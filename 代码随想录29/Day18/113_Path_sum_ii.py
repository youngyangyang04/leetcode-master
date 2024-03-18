# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # Base case: If the current node is None, there is no path, return False
        if not root:
            return False

        # Check if the current node is a leaf and the sum equals the value of the leaf
        if not root.left and not root.right and sum == root.val:
            return True

        # Recursively check the left and right subtrees with the adjusted sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val
        )
