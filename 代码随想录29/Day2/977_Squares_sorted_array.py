class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        # initializes a list of length n with all elements set to 0
        left, right, index = 0, n - 1, n - 1
        # index: keep track of the position in the result array
        while left <= right:
            left_square, right_square = nums[left] ** 2, nums[right] ** 2

            if left_square > right_square:
                result[index] = left_square
                left += 1
            else:
                result[index] = right_square
                right -= 1

            index -= 1
        return result
