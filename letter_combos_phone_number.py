'''
17. Letter Combinations of a Phone Number
Solved
Medium
Topics
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
        
    digit_to_chars_map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g','h','i'],
                            '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r', 's'],
                            '8': ['t','u','v'], '9': ['w','x','y', 'z']}
    
    result = []
    n = len(digits)
    def recurse(cur_num, i):
        if len(cur_num) == n:
            result.append(cur_num)
            return
        
        for c in digit_to_chars_map[digits[i]]:
            recurse(f'{cur_num}{c}', i + 1)
    
    recurse("", 0)
    return result