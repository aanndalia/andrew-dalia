'''
56. Merge Intervals
Solved
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 2:
        return intervals

    res = []
    intervals = sorted(intervals)
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] > end:
            # new interval
            res.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
        else:
            # existing interval
            end = max(end, intervals[i][1])
    
    res.append([start, end])
    return res