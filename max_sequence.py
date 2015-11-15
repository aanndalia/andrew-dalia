# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 22:02:30 2014

@author: stree_001
"""

"""
Finds the maximum lenghth of an incremental sequence
"""

arr = [7, 2, 3, 1, 5, 8, 9, 6]

cur_length = 1
max_length = 1
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        cur_length += 1
        if cur_length > max_length:
            max_length = cur_length
    else:
        cur_length = 1
        
print max_length