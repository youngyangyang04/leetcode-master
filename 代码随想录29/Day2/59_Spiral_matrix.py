class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize a matrix with zeros
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # Starting point
        loop, mid = n // 2, n // 2  # Number of loops and mid for odd-sized matrix
        count = 1  # Counter for filling values

        for offset in range(
            1, loop + 1
        ):  # Iterate through each layer, starting from the outermost
            # Traverse from left to right
            for i in range(starty, n - offset):
                nums[startx][i] = count
                count += 1
            # Traverse from top to bottom
            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1
            # Traverse from right to left
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1
            # Traverse from bottom to top
            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1
            startx += 1  # Update starting point
            starty += 1

        if n % 2 != 0:  # If n is odd, fill the center point
            nums[mid][mid] = count

        return nums
