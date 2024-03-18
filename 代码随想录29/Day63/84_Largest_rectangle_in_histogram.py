class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Insert 0 at the beginning and end of the heights list to simplify boundary checks
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        # monotone-decreasing stack
        for i in range(1, len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid_height = heights[stack[-1]]
                    stack.pop()
                    if stack:
                        right_height = heights[i]
                        left_height = heights[stack[-1]]
                        h = mid_height
                        w = i - stack[-1] - 1
                        result = max(h * w, result)
                stack.append(i)
        return result
