'''
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n < 2:
        return n

    right = 1
    left = 0
    res = 1
    window_set = set([s[left]])
    while right < n:
        print(left, right, window_set, res)
        while s[right] in window_set:
            window_set.remove(s[left])
            left += 1

        res = max(res, right - left + 1)
        window_set.add(s[right])
        right += 1

    return res