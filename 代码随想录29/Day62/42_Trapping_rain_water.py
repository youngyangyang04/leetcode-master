class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]  # Initialize a stack with the index of the first element
        result = 0  # Initialize the result to accumulate the trapped water
        for i in range(
            1, len(height)
        ):  # Iterate through the heights starting from the second element
            if (
                height[i] < height[stack[-1]]
            ):  # If the current height is less than the height of the last element in the stack
                stack.append(i)  # Push the index of the current height to the stack
            elif (
                height[i] == height[stack[-1]]
            ):  # If the current height is equal to the height of the last element in the stack
                stack.pop()  # Pop the last element from the stack (to update it with the current index)
                stack.append(i)  # Push the index of the current height to the stack
            else:  # If the current height is greater than the height of the last element in the stack
                while (
                    stack and height[i] > height[stack[-1]]
                ):  # While the stack is not empty and the current height is greater than the height of the last element in the stack
                    mid_height = height[
                        stack[-1]
                    ]  # Get the height of the element at the top of the stack
                    stack.pop()  # Pop the element from the stack
                    if stack:  # If the stack is not empty
                        right_height = height[i]  # Height of the current element
                        left_height = height[
                            stack[-1]
                        ]  # Height of the element at the top of the stack
                        h = (
                            min(right_height, left_height) - mid_height
                        )  # Calculate the height of the water trapped between the current and the last elements in the stack
                        w = (
                            i - stack[-1] - 1
                        )  # Calculate the width of the trapped water
                        result += (
                            h * w
                        )  # Add the area of the trapped water to the result
                stack.append(i)  # Push the index of the current height to the stack
        return result  # Return the total trapped water
