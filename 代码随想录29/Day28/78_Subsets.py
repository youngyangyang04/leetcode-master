class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        # Add the current subset to the result
        result.append(path[:])

        # Explore subsets by iterating through the remaining elements
        for i in range(startIndex, len(nums)):
            # Include the current element in the subset
            path.append(nums[i])
            # Recursively call the backtracking function for the next element
            self.backtracking(nums, i + 1, path, result)
            # Backtrack by removing the last added element to explore other possibilities
            path.pop()
