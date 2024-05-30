'''
45. Jump Game II
Solved
Medium
Topics
Companies
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''


def jump(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return 0

    left = 0
    right = 0
    min_jumps = 0

    while right < n - 1:
        farthest_jump = 0
        for i in range(left, right + 1):
            farthest_jump = max(farthest_jump, i + nums[i])
        left = right + 1
        right = farthest_jump
        min_jumps += 1

    return min_jumps