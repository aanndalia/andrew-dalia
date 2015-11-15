# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 08:17:24 2014

@author: stree_001
"""

def longest_sorted_subarray(arr):
    i = 1
    begin = 0
    cur_len = 1
    max_len = 1
    max_subarray = [arr[0]]
    while i < len(arr):
        if arr[i] > arr[i-1]:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                max_subarray = arr[begin:(i+1)]
        else:
            cur_len = 1
            begin = i
            
        i += 1
    
    return max_len, max_subarray
    
def main():
    arr = [10, 12, 12, 10, 10, 11, 10]
    print longest_sorted_subarray(arr)
    arr = [5,6,3,8,3,2,7,5,210,11,45,81,32,23,43,1]
    print longest_sorted_subarray(arr)
    
    
main()