class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k and n == 0:
            # Ensures that the current combination has reached the desired length k
            # Ensures that the sum of elements in the current combination is equal to the target sum n
            result.append(path[:])  # Add a copy of the current path to the result
            return

        for i in range(startIndex, 10):
            # for i in range(startIndex, n - (k - len(path)) + 2):  # Optimization
            path.append(i)  # Process the current node
            self.backtracking(n - i, k, i + 1, path, result)
            path.pop()  # Backtrack, undo the processing of the current node
