# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: If root is None or root's value matches the target value
        if root is None or root.val == val:
            return root

        # If the target value is less than the current root value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        # If the target value is greater than the current root value, search in the right subtree
        elif val > root.val:
            return self.searchBST(root.right, val)

        # If the target value is not found, return None
        return None
