class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize a 2D array dp with dimensions (m + 1) x (n + 1) to store the maximum count of strings
        # that can be formed with at most m 0's and n 1's
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate through each string in strs
        for string in strs:
            # Count the number of ones and zeroes in the current string
            ones = string.count("1")
            zeroes = string.count("0")

            # Iterate from m to zeroes, and from n to ones, updating dp[i][j] with the maximum count of strings
            # that can be formed considering the current string
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    # Update dp[i][j] with the maximum between its current value and the value obtained by
                    # considering the current string
                    dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)

        # Return the maximum count of strings that can be formed with at most m 0's and n 1's
        return dp[m][n]
