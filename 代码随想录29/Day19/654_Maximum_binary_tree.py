# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: If there is only one element in nums
        if len(nums) == 1:
            return TreeNode(nums[0])

        # Find the maximum value and its index in nums
        max_value = max(nums)
        index = nums.index(max_value)

        # Create a new TreeNode with the maximum value
        node = TreeNode(max_value)

        # Recursively construct the left subtree
        if index > 0:
            node.left = self.constructMaximumBinaryTree(nums[:index])

        # Recursively construct the right subtree
        if index < len(nums) - 1:
            node.right = self.constructMaximumBinaryTree(nums[index + 1 :])

        return node
