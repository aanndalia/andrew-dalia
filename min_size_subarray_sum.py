'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
'''

def minSubArrayLen(target: int, nums: List[int]) -> int:
    if not nums:
        return 0

    sum_nums = sum(nums)
    if sum_nums < target:
        return 0

    n = len(nums)
    if sum_nums == target:
        return n

    left = 0
    right = 0
    cur_sum = nums[0]
    min_window = n
    while left < n and right < n:
        # print(left, right, cur_sum, min_window)
        if cur_sum >= target:
            window_size = right - left + 1
            min_window = min(min_window, window_size)
            cur_sum -= nums[left]
            if left < n:
                left += 1
        else:
            right += 1
            if right < n:
                cur_sum += nums[right]

    return min_window