class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initialize a 2D array to store the dynamic programming states
        # dp[i][0]: represents the maximum profit on day i holding a stock
        # dp[i][1]: represents the maximum profit on day i without holding any stock and not cooling down
        # dp[i][2]: represents the maximum profit on day i without holding any stock and cooling down
        # dp[i][3]: represents the maximum profit on day i without holding any stock and cooling down for 2 days
        dp = [[0] * 4 for _ in range(len(prices))]

        # Initialize the base case for the first day
        dp[0][0] = -prices[0]  # Buying on the first day
        dp[0][1] = 0  # Not holding any stock and not cooling down
        dp[0][2] = 0  # Not holding any stock and cooling down
        dp[0][3] = 0  # Not holding any stock and cooling down for 2 days

        # Iterate through the prices array starting from the second day
        for i in range(1, len(prices)):
            # Update the states for each day based on the previous states and current prices
            dp[i][0] = max(
                dp[i - 1][0], dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]
            )
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = max(dp[i - 1][0] + prices[i], dp[i - 1][2])
            dp[i][3] = dp[i - 1][2]

        # Return the maximum profit among the states on the last day
        return max(dp[-1][1], dp[-1][2], dp[-1][3])
