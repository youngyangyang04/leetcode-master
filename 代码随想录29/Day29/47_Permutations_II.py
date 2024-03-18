class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []  # List to store unique permutations
        path = []  # Current path being explored
        nums.sort()  # Sort the input nums to handle duplicates
        self.backtracking(nums, path, [False] * len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])  # Add a copy of the current path to the result
            return

        for i in range(len(nums)):
            # Skip duplicates to avoid generating duplicate subsets
            if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]) or used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False
