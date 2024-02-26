class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            # Check if the current temperature is warmer than the temperature at the index
            # represented by the top of the stack. If yes, update the result for that index.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()  # Pop the index of the temperature from the stack
                result[idx] = (
                    i - idx
                )  # Calculate the difference in indices to get the number of days
            stack.append(i)  # Append the current index to the stack

        return result
