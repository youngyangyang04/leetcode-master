class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])  # Add a copy of the current path to the result
            return

        for i in range(startIndex, n + 1):
            #    for i in range(startIndex, n - (k - len(path)) + 2):  # Optimization
            path.append(i)  # Process the current node
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # Backtrack, undo the processing of the current node
