# 解法3
#将第12行备注的’执行前半部分‘改为执行’后半部分‘
# 1、首先，在 nums 数组中二分查找得到第一个大于等于 target的下标（左边界）与第一个大于target的下标（右边界）；
# 2、如果左边界<= 右边界，则返回 [左边界, 右边界]。否则返回[-1, -1]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums:List[int], target:int, lower:bool) -> int:
            left, right = 0, len(nums)-1
            ans = len(nums)
            while left<=right: # 不变量：左闭右闭区间
                middle = left + (right-left) //2
                # lower为True，执行前半部分，找到第一个大于等于 target的下标 ，否则找到第一个大于target的下标
                if nums[middle] > target or (lower and nums[middle] >= target):
                    right = middle - 1
                    ans = middle
                else:
                    left = middle + 1
            return ans

        leftBorder = binarySearch(nums, target, True) # 搜索左边界
        rightBorder = binarySearch(nums, target, False) -1  # 搜索右边界
        if leftBorder<= rightBorder and rightBorder< len(nums) and nums[leftBorder] == target and  nums[rightBorder] == target:
            return [leftBorder, rightBorder]
        return [-1, -1]