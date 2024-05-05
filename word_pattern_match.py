'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''


def wordPattern(pattern: str, s: str) -> bool:
    if not s or not pattern:
        return False

    words = s.split(' ')
    if len(words) != len(pattern):
        return False

    word_map = {}
    patterns_used_set = set()
    for i, word in enumerate(words):
        if word in word_map:
            if word_map[word] != pattern[i]:
                return False
        else:
            if pattern[i] in patterns_used_set:
                return False

            word_map[word] = pattern[i]
            patterns_used_set.add(pattern[i])

    return True