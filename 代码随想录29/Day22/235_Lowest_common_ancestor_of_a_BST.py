# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Helper function for recursive traversal
        def traversal(curr):
            # Base case: if current node is None, return None
            if curr is None:
                return None

            # If current node's value is greater than both p and q
            if curr.val > p.val and curr.val > q.val:
                # Recur on the left child
                return traversal(curr.left)
            # If current node's value is less than both p and q
            elif curr.val < p.val and curr.val < q.val:
                # Recur on the right child
                return traversal(curr.right)
            else:
                # Current node is the lowest common ancestor
                return curr

        # Start traversal from the root
        return traversal(root)
