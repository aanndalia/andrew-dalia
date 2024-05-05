'''
22. Generate Parentheses
Solved
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
'''


def generateParenthesis(n: int) -> List[str]:
    res = set()
    stack = []
    def backtrack(open_left, close_left):
        if open_left == close_left == 0:
            res.add(''.join(stack))
            return

        if open_left:
            stack.append('(')
            backtrack(open_left - 1, close_left)
            stack.pop(-1)

        if close_left > open_left:
            stack.append(')')
            backtrack(open_left, close_left - 1)
            stack.pop(-1)

    backtrack(n, n)
    return res