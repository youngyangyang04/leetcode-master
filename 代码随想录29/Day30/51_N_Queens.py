from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessboard = [
            ["." for _ in range(n)] for _ in range(n)
        ]  # Initialize chessboard

        def is_valid(row, col, chessboard, n):
            # Check if placing a queen at (row, col) is valid
            for i in range(row):
                if (
                    chessboard[i][col] == "Q"
                    or (col - (row - i) >= 0 and chessboard[i][col - (row - i)] == "Q")
                    or (col + (row - i) < n and chessboard[i][col + (row - i)] == "Q")
                ):
                    return False
            return True

        def backtrack(row):
            nonlocal result
            if row == n:
                # All queens are placed successfully, add the current configuration to the result
                result.append(["".join(row) for row in chessboard])
                return

            for i in range(n):
                if is_valid(row, i, chessboard, n):
                    chessboard[row][i] = "Q"
                    backtrack(row + 1)
                    chessboard[row][i] = "."

        backtrack(0)
        return result
