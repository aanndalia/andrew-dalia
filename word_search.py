'''
79. Word Search
Solved
Medium
Topics 
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''


def word_search(board: List[List[str]], word: str) -> bool:
    if not word:
        return True
    
    if not board:
        return False

    nrows = len(board)
    ncols = len(board[0])

    def inbounds(r, c):
        if r >= 0 and r < nrows and c >= 0 and c < ncols:
            return True
        
        return False


    def dfs(row, col, visited, word_index):
        if word_index == len(word):
            return True
        
        if not inbounds(row, col) or (row, col) in visited or board[row][col] != word[word_index]:
            return False
        
        visited.add((row, col))
        if dfs(row + 1, col, visited, word_index + 1) or dfs(row - 1, col, visited, word_index + 1) or dfs(row, col + 1, visited, word_index + 1) or dfs(row, col - 1, visited, word_index + 1):
            return True

        visited.remove((row, col))
        return False
    
    for row_num in range(nrows):
        for col_num in range(ncols):
            if dfs(row_num, col_num, set(), 0):
                return True
    
    return False