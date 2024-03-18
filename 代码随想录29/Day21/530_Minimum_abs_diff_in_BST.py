# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = float("inf")
        # Initialize a variable to keep track of the previous node during traversal
        self.pre = None

    def traversal(self, cur):
        # Recursive function for in-order traversal of the binary search tree
        if cur is None:
            return

        # Traverse the left subtree
        self.traversal(cur.left)

        # Check the difference between the current node value and the previous node value
        if self.pre is not None:
            # Update the result with the minimum difference
            self.result = min(self.result, cur.val - self.pre.val)

        # Update the previous node to the current node
        self.pre = cur

        # Traverse the right subtree
        self.traversal(cur.right)

    def getMinimumDifference(self, root):
        # Entry point for calculating the minimum difference
        self.traversal(root)
        # Return the final result
        return self.result
