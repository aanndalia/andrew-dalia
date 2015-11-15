# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 02:25:11 2015

@author: stree_001
"""

def min_diff(x, y):
    i = 0
    j = 0
    min_diff = float('inf')
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            if y[j] - x[i] < min_diff:
                min_diff = y[j] - x[i]
            i += 1
        else:
            if x[i] - y[j] < min_diff:
                min_diff = x[i] - y[j]
            j += 1
            
    return min_diff
    
    
print min_diff([1,2,3,9], [7,10,16,19])