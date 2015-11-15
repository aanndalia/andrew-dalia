# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 08:18:57 2015

@author: stree_001
"""

# gets kth largest element from 2 sorted arrays
def get_k_largest_elem_from_2_sorted_arrays(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return None
        
    if k < 1:
        return None
        
    i1 = 0
    i2 = 0
    ind = 0
    sorter = []
    while i1 < len(arr1) and i2 < len(arr2) and i1 < k and i2 < k and len(sorter) <= k:
        print i1, i2, ind, arr1[i1], arr2[i2]
        if arr1[i1] < arr2[i2]:
            sorter.append(arr1[i1])
            i1 += 1
            ind += 1
            
        elif arr1[i1] == arr2[i2]:
            sorter.append(arr1[i1])
            sorter.append(arr2[i2])
            i1 += 1
            i2 += 1
            ind += 2
            
        else:
            sorter.append(arr2[i2])
            i2 += 1
            ind += 1
            
    while i1 < len(arr1) and i1 < k and ind < k and len(sorter) <= k:
        sorter.append(arr1[i1])
        i1 += 1
        ind += 1
        
    while i2 < len(arr2) and i2 < k and ind < k and len(sorter) <= k:
        sorter.append(arr2[i2])
        i2 += 1
        ind += 1
        
    return sorter[k-1]
    
def get_k_largest_elem_from_2_sorted_arrays_2(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return None
        
    if k < 1:
        return None
        
    i1 = 0
    i2 = 0
    ind = 0
    last = 0
    #sorter = []
    while i1 < len(arr1) and i2 < len(arr2) and i1 < k and i2 < k and ind < k:
        print i1, i2, ind, arr1[i1], arr2[i2]
        if arr1[i1] < arr2[i2]:
            last = arr1[i1]
            i1 += 1
            ind += 1
            
        elif arr1[i1] == arr2[i2]:
            last = arr1[i1]
            i1 += 1
            i2 += 1
            ind += 2
            
        else:
            last = arr2[i2]
            i2 += 1
            ind += 1
            
    while i1 < len(arr1) and i1 < k and ind < k:
        last = arr1[i1]
        i1 += 1
        ind += 1
        
    while i2 < len(arr2) and i2 < k and ind < k:
        last = arr2[i2]
        i2 += 1
        ind += 1
        
    return last

# test        
arr1 = [3,6,7,9,11,13,19]
arr2 = [1,4,8,9]
k = 8
print get_k_largest_elem_from_2_sorted_arrays(arr1, arr2, k)
print get_k_largest_elem_from_2_sorted_arrays_2(arr1, arr2, k)