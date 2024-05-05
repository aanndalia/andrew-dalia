'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i]
, you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to
the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''

def jump(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    memo = {}

    def recurse_memo(i):
        if i >= n:
            return n + 1

        if i == n - 1:
            return 0

        if i in memo:
            return memo[i]

        steps_at_j = []
        for j in range(1, 1 + nums[i]):
            j_jumps = recurse_memo(i + j) + 1
            steps_at_j.append(j_jumps)

        min_steps = min(steps_at_j + [n + 1])
        memo[i] = min_steps
        return min_steps

    res = recurse_memo(0)
    if res > n:
        return None

    return res