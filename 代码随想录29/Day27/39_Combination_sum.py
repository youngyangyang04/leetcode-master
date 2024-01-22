class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the combinations
        result = []
        # Call the backtracking function to find combinations
        self.backtracking(candidates, target, 0, 0, [], result)
        # Return the final result
        return result

    def backtracking(self, candidates, target, total, startIndex, path, result):
        # If the total exceeds the target, return
        if total > target:
            return
        # If the total equals the target, add the combination to the result
        if total == target:
            result.append(path[:])
            return

        # Iterate through candidates starting from the given index
        for i in range(startIndex, len(candidates)):
            # Include the current candidate in the combination
            total += candidates[i]
            path.append(candidates[i])

            # Recursively call backtracking with updated parameters
            self.backtracking(candidates, target, total, i, path, result)

            # Backtrack: Remove the last added candidate for the next iteration
            total -= candidates[i]
            path.pop()
