class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)  # Calculate the total sum of nums
        if abs(target) > total_sum:
            return 0  # If the absolute value of target exceeds the total sum, there's no way to achieve it
        if (target + total_sum) % 2 == 1:
            return 0  # If the sum of target and total sum is odd, there's no way to achieve it
        target_sum = (target + total_sum) // 2  # Calculate the target sum
        dp = [0] * (
            target_sum + 1
        )  # Create a dynamic programming array, initialize with zeros
        dp[0] = (
            1  # When the target sum is 0, there's only one way, i.e., not selecting anything
        )
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] += dp[j - num]  # Update the dp array based on the current number
        return dp[target_sum]  # Return the count of ways to achieve the target sum

        # sum(P) - sum(N) = target
        # sum(P) + sum(N) = sum(nums)
        # => sum(P) = (target + sum(nums)) / 2
