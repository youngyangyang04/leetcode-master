# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Special case handling - if the tree is empty. This serves as the base case for recursion.
        if not preorder:
            return None

        # Step 2: The first element in preorder is the current root node.
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Step 3: Find the index where inorder is split.
        separator_idx = inorder.index(root_val)

        # Step 4: Split the inorder array into left and right halves.
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1 :]

        # Step 5: Split the preorder array into left and right halves.
        # ⭐️ Key Point 1: The sizes of the inorder and preorder arrays are always the same.
        preorder_left = preorder[1 : 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left) :]

        # Step 6: Recursion
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        # Step 7: Return the answer
        return root
