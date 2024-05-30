'''
Meeting Schedule
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false

Explanation:
(0,30),(5,10) and (0,30),(15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 100
0 <= intervals[i].start < intervals[i].end <= 1000
Accepted: 4308  |  Submitted: 12993  |  Acceptance Rate: 33%
'''

def canAttendMeetings(intervals) -> bool:
    n = len(intervals)
    if n < 2:
        return True

    times = [False for _ in range(1000001)]
    for interval in intervals:
        for t in range(interval[0] + 1, interval[1]):
            if times[t]:
                return False

            times[t] = True

    return True


intervals = [(2,3),(1,5),(3,4)]
res=canAttendMeetings(intervals)
print(res)