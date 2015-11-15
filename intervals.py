# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 02:18:36 2015

@author: stree_001
"""

def find_intervals(intervals):
    # sort intervals by first number (start)
    intervals.sort()
    
    stack = []
    stack.append(intervals[0])
    
    for i in range(1, len(intervals)):
        top = stack[0]
        
        if intervals[i][0] > top[1]:
            # no overlap
            stack.append(intervals[i])
            
        else:
            # overlap            
            stack.pop(0)
            stack.append((top[0], intervals[i][1]))
    
    return stack
    
    
#intervals = [(1,3),(7,9),(4,6),(10,13)]
#intervals = [(6,8),(1,3),(2,4),(4,7)]
intervals = [(6,8), (1,9), (2,4), (4,7)]
ints = find_intervals(intervals)
print ints