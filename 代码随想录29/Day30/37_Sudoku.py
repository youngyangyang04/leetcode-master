class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(row, col, num, board):
            # Check if placing 'num' at (row, col) is valid
            for i in range(9):
                if (
                    board[row][i] == num
                    or board[i][col] == num
                    or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num
                ):
                    return False
            return True

        def backtracking():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in map(str, range(1, 10)):
                            if is_valid(i, j, k, board):
                                board[i][j] = k
                                if backtracking():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        backtracking()
