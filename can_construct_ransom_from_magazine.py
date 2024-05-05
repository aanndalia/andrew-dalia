'''
383. Ransom Note
Solved
Easy
Topics
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''


def canConstruct(ransomNote: str, magazine: str) -> bool:
    if not ransomNote:
        return True

    if len(ransomNote) > len(magazine):
        return False

    if ransomNote == magazine:
        return True

    ransom_freq = [0 for i in range(26)]
    magazine_freq = [0 for i in range(26)]
    for m in magazine:
        bucket = ord(m) - ord('a')
        magazine_freq[bucket] += 1

    for r in ransomNote:
        bucket = ord(r) - ord('a')
        ransom_freq[bucket] += 1

    for i in range(26):
        if ransom_freq[i] > magazine_freq[i]:
            return False

    return True