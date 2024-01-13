# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Special case handling - if the tree is empty (recursive base case)
        if not postorder:
            return None

        # Step 2: The last element in postorder is the current root node.
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Step 3: Find the index where inorder is split.
        separator_idx = inorder.index(root_val)

        # Step 4: Split the inorder array into left and right halves.
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1 :]

        # Step 5: Split the postorder array into left and right halves.
        # ⭐️ Key Point 1: The sizes of the inorder and postorder arrays are always the same.
        postorder_left = postorder[: len(inorder_left)]
        postorder_right = postorder[len(inorder_left) : len(postorder) - 1]

        # Step 6: Recursion
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        # Step 7: Return the answer
        return root
