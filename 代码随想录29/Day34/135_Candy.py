from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Initialize candies for each child to 1
        candy = len(ratings) * [1]

        # Forward pass to give more candies to higher-rated child if needed
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                # If the current child has a higher rating than the previous one,
                # give them one more candy than the previous child
                candy[i] = candy[i-1] + 1

        # Backward pass to make sure lower-rated child gets more candies if needed
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # If the current child has a higher rating than the next one,
                # and if their current candy count is not maximum, update it
                candy[i] = max(candy[i+1] + 1, candy[i])

        # Calculate the total number of candies needed
        result = sum(candy)
        return result