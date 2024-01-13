# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_depth = float("-inf")
        self.result = None

        # Start the traversal from the root with depth 0
        self.traversal(root, 0)

        # Return the result after traversal
        return self.result

    def traversal(self, node, depth):
        # Check if the current node is a leaf node
        if not node.left and not node.right:
            # Update result if the current depth is greater than max_depth
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return

        # Recursive traversal for the left child if it exists
        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1

        # Recursive traversal for the right child if it exists
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1
