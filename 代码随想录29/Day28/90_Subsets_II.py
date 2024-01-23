class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        # Sort the input array to handle duplicates
        nums.sort()
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        # Add the current subset to the result
        result.append(path[:])

        # Explore subsets by iterating through the remaining elements
        for i in range(startIndex, len(nums)):
            # Skip duplicates to avoid generating duplicate subsets
            if i > startIndex and nums[i] == nums[i - 1]:
                continue

            # Include the current element in the subset
            path.append(nums[i])
            # Recursively call the backtracking function for the next element
            self.backtracking(nums, i + 1, path, result)
            # Backtrack by removing the last added element to explore other possibilities
            path.pop()
