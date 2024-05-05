'''
200. Number of Islands
Solved
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    m = len(grid)
    n = len(grid[0])
    visited = set()

    def valid(r, c):
        if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] != '0' and (r, c) not in visited:
            return True

        return False

    num_islands = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == '0':
                continue

            if (row, col) in visited:
                continue

            # print(row, col, num_islands, visited)
            q = [(row, col)]
            while q:
                r, c = q.pop(0)
                # print(r, c, num_islands, visited)
                if valid(r + 1, c):
                    q.append((r + 1, c))
                if valid(r - 1, c):
                    q.append((r - 1, c))
                if valid(r, c + 1):
                    q.append((r, c + 1))
                if valid(r, c - 1):
                    q.append((r, c - 1))

                visited.add((r, c))

            num_islands += 1

    return num_islands