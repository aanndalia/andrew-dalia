'''
84. Largest Rectangle in Histogram
Solved
Hard
Topics
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''


def largestRectangleArea(heights: List[int]) -> int:
    # as long as heights are increasing there's no need to pop
    max_area = 0
    left_extent_idx_stack = []
    for i, height in enumerate(heights):
        start = i
        while left_extent_idx_stack and height < left_extent_idx_stack[-1][1]:
            left_idx, left_height = left_extent_idx_stack.pop(-1)
            max_area = max(max_area, left_height * (i - left_idx))
            start = left_idx

        left_extent_idx_stack.append((start, height))

    while left_extent_idx_stack:
        left_idx, left_height = left_extent_idx_stack.pop(-1)
        max_area = max(max_area, left_height * (i - left_idx + 1))

    return max_area