class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        window_indices = []

        for i, num in enumerate(nums):
            # Remove elements outside of the current window
            while window_indices and window_indices[0] < i - k + 1:
                window_indices.pop(0)

            # Remove elements smaller than the current element from the back
            while window_indices and nums[window_indices[-1]] < num:
                window_indices.pop()

            # Add the current element index to the list
            window_indices.append(i)

            # Add the maximum element for the current window to the result
            if i >= k - 1:
                result.append(nums[window_indices[0]])

        return result
