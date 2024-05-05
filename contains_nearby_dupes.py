'''
219. Contains Duplicate II
Easy
Topics
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    if not nums:
        return False

    n = len(nums)
    num_to_idx_map = {}
    for i, num in enumerate(nums):
        if num in num_to_idx_map:
            if i - num_to_idx_map[num] <= k:
                return True
            else:
                num_to_idx_map[num] = i
        else:
            num_to_idx_map[num] = i

    return False