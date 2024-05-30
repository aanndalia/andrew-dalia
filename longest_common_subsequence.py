'''
Longest Common Subsequence
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:

Input: text1 = "cat", text2 = "crabt"

Output: 3
Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:

Input: text1 = "abcd", text2 = "abcd"

Output: 3
Example 3:

Input: text1 = "abcd", text2 = "efgh"

Output: 0
Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

'''


def longestCommonSubsequence(text1: str, text2: str) -> int:
    if not text1 or not text2:
        return 0

    n1 = len(text1)
    n2 = len(text2)
    dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]
    for i2 in range(1, n2 + 1):
        for i1 in range(1, n1 + 1):
            if text1[i1 - 1] == text2[i2 - 1]:
                dp[i2][i1] = dp[i2 - 1][i1 - 1] + 1
            else:
                dp[i2][i1] = max(dp[i2 - 1][i1], dp[i2][i1 - 1])

    # print(dp)
    res = dp[-1][-1]
    return res