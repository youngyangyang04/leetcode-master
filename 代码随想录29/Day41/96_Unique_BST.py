class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
                # Update dp[i] with the maximum of three possibilities
                # 1. j multiplied by the remaining (i - j) part
                # 2. j multiplied by the maximum product of the remaining part (dp[i - j])
                # 3. The current maximum product for i
        return dp[n]
