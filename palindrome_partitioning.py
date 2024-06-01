'''
131. Palindrome Partitioning
Solved
Medium
Topics
Companies
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''


def partition(s: str) -> List[List[str]]:
    if not s:
        return []

    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
    n = len(s)
    res = []
    partition = []
    def dfs(i):
        if i == n:
            res.append(partition.copy())
            return
        
        for j in range(i, n):
            if is_palindrome(i, j):
                partition.append(s[i:j + 1])
                dfs(j + 1)
                partition.pop()
    
    dfs(0)
    return res