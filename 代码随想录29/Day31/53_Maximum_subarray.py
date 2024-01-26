class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]  # Initialize result to the first element of nums
        count = 0
        for num in nums:
            count += num
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result
