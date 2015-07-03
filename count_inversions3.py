# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 19:16:56 2015

@author: stree_001
"""

def count_inversions(arr):
    if len(arr) == 0:
        return None, None
        
    if len(arr) == 1:
        return arr, 0
     
    mid = len(arr) / 2
    print arr, mid
    left, lcount = count_inversions(arr[0:mid])
    right, rcount = count_inversions(arr[mid:])
    
    output, mcount = merge_count(left, right)
    return output, lcount + rcount + mcount
    
def merge_count(left, right):
    output = []
    r = 0
    p = 0
    icount = 0
    while p < len(left) and r < len(right):
        if left[p] < right[r]:
            output.append(left[p])
            p += 1
        elif left[p] == right[r]:
            output.append(left[p])
            output.append(right[r])
            p += 1
            r += 1
        else:
            output.append(right[r])
            r += 1
            icount += (len(left) - p)
            
    while p < len(left):
        output.append(left[p])
        p += 1
    
    while r < len(right):
        output.append(right[r])
        r += 1
        
    return output, icount
    
def main():
    arr = [2,7,8,3,4]
    print count_inversions(arr)
    
main()