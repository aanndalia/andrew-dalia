'''
213. House Robber II
Solved
Medium
Topics
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''


def rob(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    # solve house_robber excluding first house
    max_from_next_2 = nums[-1]
    max_from_next = max(nums[-2], nums[-1])
    for i in range(n - 3, 0, -1):
        temp = max_from_next
        max_from_next = max(nums[i] + max_from_next_2, max_from_next)
        max_from_next_2 = temp

    max_exclude_first = max(max_from_next, max_from_next_2)

    # solve house_robber excluding last house
    max_from_next_2 = nums[-2]
    max_from_next = max(nums[-3], nums[-2])
    for i in range(n - 4, -1, -1):
        temp = max_from_next
        max_from_next = max(nums[i] + max_from_next_2, max_from_next)
        max_from_next_2 = temp

    max_exclude_last = max(max_from_next, max_from_next_2)

    # take max of both solutions
    res = max(max_exclude_first, max_exclude_last)
    return res