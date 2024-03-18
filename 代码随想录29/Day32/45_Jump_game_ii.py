class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize current and next distances
        curDistance = 0
        nextDistance = 0
        # Initialize result to count the number of jumps
        result = 0

        # If there is only one element in the array, no jumps needed
        if len(nums) == 1:
            return 0

        # Iterate through the array
        for i in range(len(nums)):
            # Update the next possible distance we can reach
            nextDistance = max(i + nums[i], nextDistance)

            # If we have reached the current distance, we need to jump
            if i == curDistance:
                # Increment the result to count the jump
                result += 1
                # Update the current distance to the next possible distance
                curDistance = nextDistance
                # If the current distance is beyond or equal to the last index, no more jumps needed
                if curDistance >= len(nums) - 1:
                    break

        # Return the total number of jumps needed
        return result
