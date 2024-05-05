'''
739. Daily Temperatures
Solved
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # stack of indices of the days that need to find a higher number later in the list
    days_needing_warmer_stack = []
    res = [0 for _ in range(len(temperatures))]
    for i, temp in enumerate(temperatures):
        while days_needing_warmer_stack and temp > temperatures[days_needing_warmer_stack[-1]]:
            idx_to_update = days_needing_warmer_stack.pop(-1)
            res[idx_to_update] = i - idx_to_update

        days_needing_warmer_stack.append(i)

    return res