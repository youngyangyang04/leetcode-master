class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get the lengths of the input words
        m, n = len(word1), len(word2)

        # Initialize the dynamic programming table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp table
        for i in range(m + 1):
            for j in range(n + 1):
                # Base case: if one of the words is empty
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                # If characters match, take the value from diagonal
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # If characters don't match, take the minimum of left, top, and diagonal + 1
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1
                    )

        # Return the bottom-right corner value of dp table
        return dp[m][n]
