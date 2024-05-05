'''
90. Subsets II
Solved
Medium
Topics
Companies
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = set()

    def recurse(i, cur):
        if i >= len(nums):
            return

        res.add(tuple(cur))
        res.add(tuple(cur + [nums[i]]))

        # don't take nums[i]
        recurse(i + 1, cur)

        # take nums[i]
        recurse(i + 1, cur + [nums[i]])

    nums = sorted(nums)
    recurse(0, [])
    return list(res)