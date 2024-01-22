class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Initialize an empty list to store the partitions
        result = []
        # Call the backtracking function to find partitions
        self.backtracking(s, 0, [], result)
        # Return the final result
        return result

    def backtracking(self, s, startIndex, path, result):
        # If the current substring is processed, add the partition to the result
        if startIndex == len(s):
            result.append(path[:])
            return

        # Iterate through substrings starting from the given index
        for i in range(startIndex, len(s)):
            # Check if the substring is a palindrome
            if self.is_palindrome(s, startIndex, i):
                # Include the palindrome substring in the partition
                path.append(s[startIndex : i + 1])
                # Recursively call backtracking with updated parameters
                self.backtracking(s, i + 1, path, result)
                # Backtrack: Remove the last added substring for the next iteration
                path.pop()

    def is_palindrome(self, s: str, start: int, end: int):
        # Check if the substring is a palindrome
        i: int = start
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
