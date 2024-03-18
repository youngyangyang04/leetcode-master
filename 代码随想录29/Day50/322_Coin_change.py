class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create dynamic programming array, initialize with positive infinity
        dp = [float("inf")] * (amount + 1)
        # Initialize the minimum number of coins for a backpack capacity of 0 to be 0
        dp[0] = 0

        # Iterate through the list of coins, akin to iterating through items
        for coin in coins:
            # Iterate through the backpack capacity
            for i in range(coin, amount + 1):
                # If dp[i - coin] is not the initial value, perform state transition
                if dp[i - coin] != float("inf"):
                    # Update the minimum number of coins
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        # If the final minimum number of coins for the backpack capacity is still positive infinity, it means there is no solution
        if dp[amount] == float("inf"):
            return -1
        # Return the minimum number of coins for the backpack capacity of 'amount'
        return dp[amount]
