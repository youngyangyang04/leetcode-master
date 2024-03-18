class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        # Check if the intervals list is empty
        if len(intervals) == 0:
            return result  # Return an empty list, as there are no intervals to merge

        # Sort intervals based on the start times
        intervals.sort(key=lambda x: x[0])

        # Initialize the result with the first interval
        result.append(intervals[0])

        # Iterate through the sorted intervals starting from the second interval
        for i in range(1, len(intervals)):
            # Check if the current interval overlaps with the last interval in the result
            if intervals[i][0] <= result[-1][1]:
                # Merge overlapping intervals by updating the end time
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                # Add non-overlapping intervals to the result
                result.append(intervals[i])

        return result
