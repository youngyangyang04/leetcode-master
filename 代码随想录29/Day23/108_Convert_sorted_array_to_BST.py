# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def traversal(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = traversal(left, mid - 1)
            node.right = traversal(mid + 1, right)
            return node

        return traversal(0, len(nums) - 1)
