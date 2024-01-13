# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(node, count):
            # Check if the current node is a leaf
            if not node.left and not node.right:
                # Check if the remaining count equals the value of the current leaf
                return count == node.val

            # Update count for the left child if it exists
            left_result = False
            if node.left:
                left_result = traversal(node.left, count - node.val)

            # Update count for the right child if it exists
            right_result = False
            if node.right:
                right_result = traversal(node.right, count - node.val)

            # Return True if either left or right subtree has a path sum
            return left_result or right_result

        # Check if the root is None
        if not root:
            return False

        # Start traversal from the root with the initial count as the targetSum
        return traversal(root, targetSum)
