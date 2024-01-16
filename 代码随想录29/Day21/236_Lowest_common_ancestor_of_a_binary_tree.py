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
        # Base case: if the root is None or matches either of the nodes, it is the ancestor
        if root is None or root == p or root == q:
            return root

        # Recursive traversal of the left subtree
        left_ancestor = self.lowestCommonAncestor(root.left, p, q)

        # Recursive traversal of the right subtree
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)

        # Check if both nodes are found in different subtrees
        if left_ancestor is not None and right_ancestor is not None:
            return root  # The current root is the lowest common ancestor

        # If one of the nodes is found in the right subtree
        elif left_ancestor is None and right_ancestor is not None:
            return right_ancestor

        # If one of the nodes is found in the left subtree
        elif left_ancestor is not None and right_ancestor is None:
            return left_ancestor

        # If neither node is found in the subtrees
        else:
            return None
