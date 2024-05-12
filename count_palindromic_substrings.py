'''
647. Palindromic Substrings
Solved
Medium
Topics
Companies
Hint
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

def countSubstrings(s: str) -> int:
    if len(s) < 2:
        return len(s)

    total = 0
    for i in range(len(s)):
        left = i
        right = i
        while left > -1 and right < len(s) and s[left] == s[right]:
            total += 1
            left -= 1
            right += 1
        
    for i in range(len(s) - 1):
        left = i
        right = i + 1
        while left > -1 and right < len(s) and s[left] == s[right]:
            total += 1
            left -= 1
            right += 1

    return total