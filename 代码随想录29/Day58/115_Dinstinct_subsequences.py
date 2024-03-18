class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # Base case: if t is empty, there's exactly one way to match any non-empty s to an empty t
        for i in range(m):
            dp[i][0] = 1

        # Base case: if s is empty, there's no way to match any non-empty t
        for j in range(1, n):
            dp[0][j] = 0

        # Fill in the dp table using dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current characters of s and t match, we have two options:
                # 1. Use the current characters as part of the subsequence (dp[i - 1][j - 1])
                # 2. Ignore the current character of s and look for a match in the remaining s (dp[i - 1][j])
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If the characters don't match, we can only ignore the current character of s
                    dp[i][j] = dp[i - 1][j]

        # The bottom-right cell of the dp table stores the result
        return dp[-1][-1]
