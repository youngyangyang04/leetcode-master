class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prediff = 0
        curdiff = 0
        result = 1
        for i in range(len(nums) - 1):
            curdiff = nums[i + 1] - nums[i]
            if (prediff >= 0 and curdiff < 0) or (prediff <= 0 and curdiff > 0):
                result += 1
                prediff = curdiff  # deal with the monotony with a flat gradient
        return result
