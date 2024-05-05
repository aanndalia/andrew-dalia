'''
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


def climbStairs(n: int) -> int:
    if n < 3:
        return n

    ways_from_one_step = 1
    ways_from_two_step = 1
    for _ in range(n - 1):
        temp = ways_from_one_step
        ways_from_one_step = ways_from_one_step + ways_from_two_step
        ways_from_two_step = temp

    return ways_from_one_step