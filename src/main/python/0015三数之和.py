

"""
# 第15题. 三数之和

[力扣题目链接](https://leetcode.cn/problems/3sum/)

给你一个包含 n 个整数的数组nums，判断  nums  中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

**注意：** 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

#思路：指针

from typing import List

class Solution:
    def treeSum(self, nums:List[int], target:int) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range( n ):
            left = i + 1
            right = n - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr > 0:
                    right -= 1
                if curr < 0:
                    left += 1
                else:
                    ans.append( [nums[i], nums[left], nums[right] ])
                    # 去重
                    while left != right and nums[left-1] == nums[left]:
                        left += 1
                    while left != right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans






if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    ans = Solution().treeSum( nums, target)
    print('ans: ', ans)


