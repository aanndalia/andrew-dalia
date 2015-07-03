# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 08:34:39 2015

@author: stree_001
"""

def longest_increasing_subsequence_slow(arr):
    if len(arr) < 2:
        return 0, 0
        
    longest = 0
    start = 0
    end = 0
    for i in range(len(arr)):
        j = i + 1
        count = 0
        print count, longest, end, start, i, j
        while j < len(arr) and arr[j] < arr[j-1]:
            count += 1
            if count > longest:
                start = i
                end = j
                longest = count
            j += 1
                
    return start, end
    
def longest_increasing_subsequence(arr):
    if len(arr) < 2:
        return 0, 0
        
    longest = 0
    start = 0
    end = 0
    best_start = 0
    count = 0
    for i in range(1, len(arr)):
        #print count, longest, end, start, best_start
        if arr[i] > arr[i-1]:
            count += 1
            #print count, longest, end, start, best_start
            if count > longest:
                longest = count
                end = i
                best_start = start
        else:
            start = i
            count = 0
            
    return best_start, end
    
def main():
    arr = [10,3,7,9,0,15]
    print longest_increasing_subsequence_slow(arr)
    print longest_increasing_subsequence(arr)
    
main()