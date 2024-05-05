'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''


def trap(height: List[int]) -> int:
    trapped_water = 0
    left = 0
    right = len(height) - 1
    max_left = height[left]
    max_right = height[right]
    while left <= right:
        if max_left <= max_right:
            trapped_water += max(0, max_left - height[left])
            max_left = max(max_left, height[left])
            left += 1
        else:
            trapped_water += max(0, max_right - height[right])
            max_right = max(max_right, height[right])
            right -= 1

    return trapped_water