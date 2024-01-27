class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):  # start from the second day
            result += max(prices[i] - prices[i - 1], 0)
        return result
