'''
78. Subsets
Solved
Medium
Topics
Companies
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''


def subsets(nums: List[int]) -> List[List[int]]:
    res = set()
    n = len(nums)

    def recurse(i, cur):
        if i >= n:
            return

        res.add(tuple(cur))
        res.add(tuple(cur + [nums[i]]))
        recurse(i + 1, cur)
        recurse(i + 1, cur + [nums[i]])

    recurse(0, [])
    return list(res)