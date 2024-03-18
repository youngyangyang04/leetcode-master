class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[0] * 5 for _ in range(len(prices))]  # Initialize dp array
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        for i in range(1, len(prices)):
            # Resting after not buying/selling
            dp[i][0] = dp[i - 1][0]
            # Buying 1st stock or not buying on i-th day
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            # Selling 1st stock or not selling on i-th day
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            # Buying 2nd stock or not buying on i-th day
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            # Selling 2nd stock or not selling on i-th day
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        return dp[-1][4]
