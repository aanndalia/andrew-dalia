'''
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
'''


def minWindow(s: str, t: str) -> str:
    from collections import defaultdict
    def freq_satisfied(f1, f2):
        for i, f in enumerate(f1):
            if f < f2[i]:
                return False

        return True

    if s == t:
        return s

    if len(t) > len(s):
        return ''

    t_freq = [0 for _ in range(60)]
    for c in t:
        t_freq[ord(c) - ord('A')] += 1

    s_freq = [0 for _ in range(60)]
    for c in s:
        s_freq[ord(c) - ord('A')] += 1

    if not freq_satisfied(s_freq, t_freq):
        return ''

    s_freq = [0 for _ in range(60)]

    res = s
    left = 0
    right = 0
    s_freq[ord(s[left]) - ord('A')] += 1
    while right < len(s):
        if freq_satisfied(s_freq, t_freq):
            res = s[left: right + 1] if right - left + 1 < len(res) else res
            s_freq[ord(s[left]) - ord('A')] -= 1
            left += 1
        else:
            right += 1
            if right >= len(s):
                break

            s_freq[ord(s[right]) - ord('A')] += 1

    return res