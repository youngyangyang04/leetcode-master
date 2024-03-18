class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        # dp[i][0]: represents the maximum profit on day i holding a stock
        # dp[i][1]: represents the maximum profit on day i without holding any stock
        dp = [[0] * 2 for _ in range(len(prices))]

        # Initialize the base case for the first day
        dp[0][0] = -prices[0]  # Buying on the first day
        dp[0][1] = 0  # Not holding any stock

        # Iterate through the prices array starting from the second day
        for i in range(1, len(prices)):
            # Update the states for each day based on the previous states and current prices
            dp[i][0] = max(
                dp[i - 1][0], dp[i - 1][1] - prices[i]
            )  # Maximizing profit while holding stock
            dp[i][1] = max(
                dp[i - 1][1], dp[i - 1][0] + prices[i] - fee
            )  # Maximizing profit without holding stock

        # Return the maximum profit without holding any stock on the last day
        return dp[-1][1]
