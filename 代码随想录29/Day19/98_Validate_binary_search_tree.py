class Solution:
    def __init__(self):
        self.maxVal = float(
            "-inf"
        )  # Initialize max value with negative infinity due to the possibility of the smallest integer value in the test data.

    def isValidBST(self, root):
        # Base case: If the root is None, it's a valid BST
        if root is None:
            return True

        # Recursively check the left subtree
        left = self.isValidBST(root.left)

        # In-order traversal: Validate that the current node's value is greater than the previously visited node's value
        if self.maxVal < root.val:
            self.maxVal = root.val
        else:
            return False

        # Recursively check the right subtree
        right = self.isValidBST(root.right)

        # Return True only if both left and right subtrees are valid BSTs
        return left and right
