class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []  # List to store valid subsequences
        path = []  # Current subsequence being formed
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        if len(path) > 1:  # At least two elements in the subsequence
            result.append(path[:])  # Add the current subsequence to the result list

        uset = set()  # Set to keep track of elements in the current subsequence
        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in uset:
                # Skip if the current element is less than the last element in the subsequence
                # or if the element is already present in the current subsequence
                continue

            uset.add(
                nums[i]
            )  # Add the current element to the set representing the current subsequence
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()  # Backtrack by removing the last element from the subsequence
