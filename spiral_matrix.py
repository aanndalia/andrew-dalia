'''
54. Spiral Matrix
Solved
Medium
Topics
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    nrows = len(matrix)
    ncols = len(matrix[0])
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    res = []
    while top <= bottom and left <= right:
        print(left, right, top, bottom)
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1
        if top > bottom:
            break

        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1
        if left > right:
            break

        for c in range(right, left - 1, -1):
            res.append(matrix[bottom][c])
        bottom -= 1
        if top > bottom:
            break

        for r in range(bottom, top - 1, -1):
            res.append(matrix[r][left])
        left += 1
        if left > right:
            break

    return res