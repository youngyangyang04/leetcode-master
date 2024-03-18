class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the combinations
        result = []
        candidates.sort()
        # Call the backtracking function to find combinations
        self.backtracking(candidates, target, 0, 0, [], result)
        # Return the final result
        return result

    def backtracking(self, candidates, target, total, startIndex, path, result):
        # If the total equals the target, add the combination to the result
        if total == target:
            result.append(path[:])
            return

        # Iterate through candidates starting from the given index
        for i in range(startIndex, len(candidates)):
            # Skip duplicates to avoid repeated combinations
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue
            if total + candidates[i] > target:
                break
            # Include the current candidate in the combination
            total += candidates[i]
            path.append(candidates[i])
            # Recursively call backtracking with updated parameters
            self.backtracking(candidates, target, total, i + 1, path, result)
            # Backtrack: Remove the last added candidate for the next iteration
            total -= candidates[i]
            path.pop()
