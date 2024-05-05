'''
239. Sliding Window Maximum
Solved
Hard
Topics
Companies
Hint
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''


from collections import deque
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    if k < 1:
        return []

    if k == 1:
        return nums

    n = len(nums)
    res = []
    left = 0
    right = 0
    dq = deque()
    while right < n:
        # print(left, right, dq, res)
        while dq and nums[right] > nums[dq[-1]]:
            dq.pop()

        dq.append(right)
        if dq[0] < left:
            dq.popleft()

        if right - left + 1 >= k:
            res.append(nums[dq[0]])
            left += 1

        right += 1

    return res