class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # Convert the integer to a string
        strNum = str(N)
        # flag is used to mark where to start assigning 9
        # Set to the length of the string to prevent the second for loop from executing without flag being assigned
        flag = len(strNum)

        # Traverse the string from right to left
        for i in range(len(strNum) - 1, 0, -1):
            # If the current character is smaller than the previous one, it means we need to modify the previous character
            if strNum[i - 1] > strNum[i]:
                flag = i  # Update the value of flag, record the position that needs to be modified
                # Subtract 1 from the previous character to maintain the increasing property
                strNum = strNum[: i - 1] + str(int(strNum[i - 1]) - 1) + strNum[i:]

        # Modify all characters from the position of flag and beyond to '9' to ensure the maximum increasing number
        for i in range(flag, len(strNum)):
            strNum = strNum[:i] + "9" + strNum[i + 1 :]

        # Convert the final string back to an integer and return
        return int(strNum)
