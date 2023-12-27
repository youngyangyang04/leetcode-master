class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # [left, right]
        while left <= right:
            middle = left + (right - left) // 2
            #  returns the quotient of the division rounded down to the nearest integer, index of the number in the middle

            if nums[middle] > target:
                right = middle - 1

            elif nums[middle] < target:
                left = middle + 1

            else:
                return middle
        return -1
