# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # can't find the node
        # can find the node
        # while delete the root:
        # left and right are none,
        # left not none and right is none
        # left is none and right not none
        # left and right are not none

        # Base case: if the root is None, return None (can't find the node)
        if root is None:
            return None

        # If the key to be deleted is smaller than the root's key,
        # it lies in the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If the key to be deleted is larger than the root's key,
        # it lies in the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If the key is the same as the root's key, this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children, get the inorder successor (smallest in the right subtree)
            successor = self.findSuccessor(root.right)

            # Copy the inorder successor's value to this node
            root.val = successor.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, successor.val)

        return root

    # Helper function to find the inorder successor
    def findSuccessor(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr
