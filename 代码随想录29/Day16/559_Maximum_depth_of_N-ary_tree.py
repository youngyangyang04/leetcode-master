"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        # Initialize the maximum depth to 1, considering the current node
        max_depth = 1

        # Traverse through each child of the current node
        for child in root.children:
            # Recursively calculate the depth of each child and update max_depth
            max_depth = max(max_depth, self.maxDepth(child) + 1)

        # Return the maximum depth of the current node and its children
        return max_depth
