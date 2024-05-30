'''
329. Longest Increasing Path in a Matrix
Hard
Topics
Companies
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    max_len = 0
    ROWS = len(matrix)
    COLS = len(matrix[0])
    max_len_cache = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    def valid(row_num, col_num, prev_row_num, prev_col_num, visited_set):
        if row_num >= ROWS or col_num >= COLS or row_num < 0 or col_num < 0 or (row_num, col_num) in visited or matrix[row_num][col_num] <= matrix[prev_row_num][prev_col_num]:
            return False
        return True
        
    for row in range(ROWS):
        for col in range(COLS):
            cur_max_len = 0
            visited = set()
            q = [(row, col, 1)]
            while q:
                cur_row, cur_col, path_len = q.pop(0)
                max_len = max(max_len, path_len)
                if valid(cur_row + 1, cur_col, cur_row, cur_col, visited):
                    q.append((cur_row + 1, cur_col, path_len + 1))
                if valid(cur_row - 1, cur_col, cur_row, cur_col, visited):
                    q.append((cur_row - 1, cur_col, path_len + 1))
                if valid(cur_row, cur_col + 1, cur_row, cur_col, visited):
                    q.append((cur_row, cur_col + 1, path_len + 1))
                if valid(cur_row, cur_col - 1, cur_row, cur_col, visited):
                    q.append((cur_row, cur_col - 1, path_len + 1))
            
    return max_len