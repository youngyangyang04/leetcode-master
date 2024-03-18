class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1]]:
                #  i % n is the modulo operation that calculates the remainder when i is divided by n
                idx = stack.pop()
                result[idx] = nums[i % n]
            if i < n:
                stack.append(i)
        return result
