class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Initialize a 2D array for dynamic programming
        dp = [[0] * n for _ in range(n)]

        # Iterate through the string starting from the end
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # Base case: when i == j, it's a single character and forms a palindrome of length 1
                if i == j:
                    dp[i][j] = 1
                # If characters at positions i and j are equal,
                # the length of palindrome increases by 2 (length of inner palindrome + 2)
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # If characters at positions i and j are not equal,
                # the maximum length of palindrome is the maximum of the two possibilities
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The result is stored at the top right corner of the dp array, representing the entire string
        return dp[0][n - 1]
