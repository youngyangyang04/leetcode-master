# -*coding=utf-8 -*-
# @Time : 2024/9/21 10:08
# @Author : 杨楠
# @File : two-sum.py
# @Software: PyCharm
class Solution(object):
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 直接在列表上进行哈希表操作
        for i in range(len(nums)):
            a = target - nums[i]
            try:
                position = nums.index(a)
            except ValueError:
                pass
            else:
                if position != i:
                    return [i,position]


nums = [-1,-2,-3,-4,-5]
target = -8
print(twoSum(nums, target))



