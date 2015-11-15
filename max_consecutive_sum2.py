# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 17:29:17 2014

@author: stree_001
"""

def maximum_subsequence(arr):
    max_sum = arr[0]
    cur_sum = arr[0]
    for i in range(1, len(arr)):
        if cur_sum + arr[i] > 0:
            cur_sum += arr[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
        else:
            cur_sum = arr[i]
            
    return max_sum
    
    
def main():
    arr = [-7, 6, 3, -3, 9, -4, 1, 7]
    print maximum_subsequence(arr)
    
main()

