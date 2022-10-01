/*
 * @lc app=leetcode.cn id=59 lang=golang
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode.cn/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (75.13%)
 * Likes:    835
 * Dislikes: 0
 * Total Accepted:    246.4K
 * Total Submissions: 327.9K
 * Testcase Example:  '3'
 *
 * 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3
 * 输出：[[1,2,3],[8,9,4],[7,6,5]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 *
 *
 */

// @lc code=start
func generateMatrix(n int) [][]int {
	var matrix = make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}
	matrixFilled(matrix, n)

	return matrix
}

func matrixFilled(matrix [][]int, n int) {
	for n > 0 {
		for i := len(matrix) - n; i < n; i++ {
			if i == 0 {
				matrix[len(matrix)-n][i] = 1
			} else {
				matrix[len(matrix)-n][i] = matrix[len(matrix)-n][i-1] + 1
			}
		}
		for i := len(matrix) - n + 1; i < n; i++ {
			matrix[i][n-1] = matrix[i-1][n-1] + 1
		}
		for i := n - 1; i > len(matrix)-n; i-- {
			matrix[n-1][i-1] = matrix[n-1][i] + 1
		}
		for i := n - 2; i > len(matrix)-n; i-- {
			matrix[i][len(matrix)-n] = matrix[i+1][len(matrix)-n] + 1
		}
		n--
	}
}

// @lc code=end

