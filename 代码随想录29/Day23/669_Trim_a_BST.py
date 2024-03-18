# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        def trim(node, low, high):
            if node is None:
                return None

            if node.val < low:
                # The entire left subtree can be ignored
                return trim(node.right, low, high)

            if node.val > high:
                # The entire right subtree can be ignored
                return trim(node.left, low, high)

            # Trim both left and right subtrees
            node.left = trim(node.left, low, high)
            node.right = trim(node.right, low, high)

            return node

        return trim(root, low, high)
