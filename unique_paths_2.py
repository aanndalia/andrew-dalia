'''
63. Unique paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot
include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
'''


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if not obstacleGrid:
        return 0

    if obstacleGrid[-1][-1] == 1:
        return 0

    nrows = len(obstacleGrid)
    ncols = len(obstacleGrid[0])

    grid = [[0 for _ in range(ncols)] for _ in range(nrows)]
    for col in range(ncols - 1, -1, -1):
        for row in range(nrows - 1, -1, -1):
            if col == ncols - 1 and row == nrows - 1:
                grid[row][col] = 1
                continue

            if obstacleGrid[row][col]:
                grid[row][col] = 0
            else:
                right_paths = grid[row][col + 1] if col + 1 < ncols else 0
                down_paths = grid[row + 1][col] if row + 1 < nrows else 0
                grid[row][col] = right_paths + down_paths

    res = grid[0][0]
    print(grid)
    return res