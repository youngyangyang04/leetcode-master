# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def robTree(node):
            if not node:
                return (0, 0)
            left = robTree(node.left)
            right = robTree(node.right)
            # If current node is robbed
            rob_cur = node.val + left[1] + right[1]

            # If current node is not robbed
            not_rob_cur = max(left) + max(right)
            return (rob_cur, not_rob_cur)

        result = robTree(root)
        return max(result)
