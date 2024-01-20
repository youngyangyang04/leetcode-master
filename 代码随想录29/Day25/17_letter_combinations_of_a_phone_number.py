class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Define a mapping of digits to corresponding letters
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Initialize an empty list to store the result
        result = []

        # Check if the input digits are not empty before starting the backtracking
        if digits:
            self.backtracking(digits, 0, "", digit_map, result)

        # Return the final result
        return result

    def backtracking(self, digits, index, current_combination, digit_map, result):
        # Base case: if the index reaches the length of the digits, add the current combination to the result
        if index == len(digits):
            result.append(current_combination)
            return

        # Get the current digit
        current_digit = digits[index]

        # Get the letters corresponding to the current digit
        letters = digit_map.get(current_digit, "")

        # Iterate through the letters and explore combinations
        for letter in letters:
            # Recursively call backtracking with the updated combination
            self.backtracking(
                digits, index + 1, current_combination + letter, digit_map, result
            )
