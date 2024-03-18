class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]  # Buying on day 0
        dp[0][1] = 0  # Buying on day 0
        for i in range(1, len(prices)):
            # Maximum profit if holding a stock or buy on day i
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            # Maximum profit if selling a stock or sell on day i
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]  # Maximum profit after selling on the last day
