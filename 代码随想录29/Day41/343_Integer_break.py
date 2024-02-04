class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        # Loop through the numbers from 3 to n (inclusive)
        for i in range(3, n + 1):
            # Loop through possible partitions (j) for the current number i
            for j in range(1, i):
                # Update dp[i] with the maximum of three possibilities
                # 1. j multiplied by the remaining (i - j) part
                # 2. j multiplied by the maximum product of the remaining part (dp[i - j])
                # 3. The current maximum product for i
                dp[i] = max(j * (i - j), j * dp[i - j], dp[i])
        return dp[n]
