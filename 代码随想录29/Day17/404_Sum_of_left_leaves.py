# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traversal(node, left_child_flag):
            # Base case: If the node is None, return 0
            if node is None:
                return 0

            # Check if the current node is a leaf node on the left
            if node.left is None and node.right is None and left_child_flag:
                return node.val

            # Recursively traverse the left and right subtrees
            left_sum = traversal(node.left, True)
            right_sum = traversal(node.right, False)

            return left_sum + right_sum

        # Start the traversal from the root with left_child_flag set to False
        return traversal(root, False)
