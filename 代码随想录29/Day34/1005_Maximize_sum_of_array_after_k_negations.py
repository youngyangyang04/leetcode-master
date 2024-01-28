class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        result = 0  # Initialize the result variable to store the final sum
        nums.sort(
            key=lambda x: abs(x), reverse=True
        )  # Sort the numbers in descending order based on their absolute values

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                # If the current number is negative and there are still negations to perform
                nums[i] *= -1  # Negate the current number
                k -= 1  # Reduce the count of remaining negations

        if k % 2 == 1:
            # If there are still an odd number of negations remaining, negate the smallest positive or zero value
            nums[-1] *= -1

        result = sum(nums)  # Calculate the sum of the modified array
        return result  # Return the final result
