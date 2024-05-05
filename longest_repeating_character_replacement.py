'''
424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''


def characterReplacement(s: str, k: int) -> int:
    def valid_window(char_freq_arr):
        max_val = max(char_freq_arr)
        rest = sum(char_freq_arr) - max_val
        return rest <= k

    n = len(s)
    if n <= k:
        return n

    char_freq = [0 for _ in range(26)]
    right = 0
    left = 0
    res = k
    while right < n:
        char_freq[ord(s[right]) - ord('A')] += 1
        print(left, right, res, char_freq)
        while not valid_window(char_freq):
            char_freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        res = max(res, right - left + 1)
        right += 1

    return res

