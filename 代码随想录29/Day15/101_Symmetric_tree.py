# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Check if the tree is symmetric by comparing left and right subtrees
        # If the tree is empty, it is considered symmetric
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        # First, handle the case of empty nodes
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        # Exclude the cases where the values are different
        elif left.val != right.val:
            return False

        # At this point, both left and right nodes are non-empty, and their values are the same
        # Recursive comparison for the next level
        outside = self.compare(
            left.left, right.right
        )  # Left subtree: left, Right subtree: right
        inside = self.compare(
            left.right, right.left
        )  # Left subtree: right, Right subtree: left
        isSame = (
            outside and inside
        )  # Left subtree: center, Right subtree: center (logical combination)
        return isSame
