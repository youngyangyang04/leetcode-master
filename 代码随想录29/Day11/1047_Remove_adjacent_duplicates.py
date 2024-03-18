class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []

        for char in s:
            # Check if 'result' is not empty and the current character is the same as the last one in 'result'.
            if result and char == result[-1]:
                result.pop()
            else:
                result.append(char)

        # Convert the list of characters back to a string and return the result.
        return "".join(result)
