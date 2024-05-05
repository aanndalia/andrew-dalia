'''
567. Permutation in String
Solved
Medium
Topics
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''


def checkInclusion(s1: str, s2: str) -> bool:
    def char_freq_gen(s):
        freq = [0 for _ in range(26)]
        for c in s:
            freq[ord(c) - ord('a')] += 1

        return freq

    def equal_freq(f1, f2):
        for i, f in enumerate(f1):
            if f != f2[i]:
                return False

        return True

    if len(s1) > len(s2):
        return False

    s1_len = len(s1)
    freq1 = char_freq_gen(s1)
    freq2 = [0 for _ in range(26)]
    right = 0
    left = 0
    print(freq1)
    while right < len(s2):
        freq2[ord(s2[right]) - ord('a')] += 1
        if sum(freq2) < s1_len:
            right += 1
            continue

        if equal_freq(freq1, freq2):
            return True

        right += 1
        freq2[ord(s2[left]) - ord('a')] -= 1
        left += 1

    return False