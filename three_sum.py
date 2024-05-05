'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    res = set()
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums) - 2):
        left = i + 1
        right = len(sorted_nums) - 1
        while left < right:
            cur_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if left == i or cur_sum < 0:
                left += 1
            elif right == i or cur_sum > 0:
                right -= 1
            else:
                res.add(tuple(sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])))
                left += 1
                right -= 1

    return list(res)