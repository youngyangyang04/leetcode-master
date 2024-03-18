# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def traversal(self, cur, path, result):
        # Add the current node's value to the path
        path.append(cur.val)  # middle

        # Check if the current node is a leaf node
        if not cur.left and not cur.right:
            # If it is a leaf, convert the path to a string and append it to the result
            sPath = "->".join(map(str, path))
            result.append(sPath)
            return

        # Recursively traverse the left subtree
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()  # Remove the last element to backtrack

        # Recursively traverse the right subtree
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()  # Remove the last element to backtrack

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []  # Store the final result
        path = []  # Store the current path during traversal
        if not root:
            return result  # If the tree is empty, return an empty result
        self.traversal(root, path, result)  # Start the traversal from the root
        return result
