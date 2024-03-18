class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [
            [0] * (2 * k + 1) for _ in range(len(prices))
        ]  # Initialize dp array with 2k+1 columns
        for j in range(1, 2 * k, 2):
            dp[0][j] = -prices[0]  # Initialize buying positions
        for i in range(1, len(prices)):
            for j in range(0, 2 * k - 1, 2):
                # Calculate maximum profit for buying or not buying on i-th day
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
                # Calculate maximum profit for selling or not selling on i-th day
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
        return dp[-1][2 * k]  # Return maximum profit at the end of all transactions
