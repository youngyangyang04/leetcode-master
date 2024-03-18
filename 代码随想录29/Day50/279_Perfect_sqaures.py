class Solution:
    def numSquares(self, n: int) -> int:
        # Create dynamic programming array, initialize with positive infinity
        dp = [float("inf")] * (n + 1)
        # Initialize the minimum number of perfect squares required for a number '0' to be 0
        dp[0] = 0

        # Iterate through the backpack capacity
        for i in range(1, n + 1):
            # Iterate through the perfect squares as items
            for j in range(1, int(i**0.5) + 1):
                # Update the minimum number of perfect squares required to form the number 'i'
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]
