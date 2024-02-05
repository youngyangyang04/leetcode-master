class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        dp = [0] * (target + 1)
        # Iterate through each number in nums
        for num in nums:
            # Iterate backward through the dp array to update the possibilities
            for j in range(target, num - 1, -1):
                # Update dp[j] with the maximum of its current value and the value obtained by adding the current number
                dp[j] = max(dp[j], dp[j - num] + num)

        # Check if the last element in dp is equal to the target sum, indicating a valid partition
        return dp[-1] == target
