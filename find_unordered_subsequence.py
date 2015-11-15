# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 08:18:18 2014

@author: stree_001
"""

# Find indices m and n such that if you sorted elements m through n, the
# entire array would be sorted. 
# Minimize m - n (find the smallest such sequence) [17.6]
def find_unordered_subsequence(arr):
    i = 1
    while arr[i] > arr[i-1]:
        if i >= len(arr) - 1:
            return 0, len(arr) - 1
        i += 1
    
    unsorted_begin = i
    
    j = len(arr) - 1
    while arr[j] > arr[j-1]:
        j -= 1
    unsorted_end = j - 1
    
    #print arr[unsorted_begin]
    #print arr[unsorted_end]
    left_end = unsorted_begin - 1
    right_begin = unsorted_end + 1
    
    min_unsorted = arr[unsorted_begin]
    max_unsorted = arr[unsorted_end]
    for k in range(unsorted_begin, unsorted_end+1):
        if arr[k] > max_unsorted:
            max_unsorted = arr[k]
        elif arr[k] < min_unsorted:
            min_unsorted = arr[k]
            
    #if left_end >= 0:        
    while (left_end >= 0 and arr[left_end] > min_unsorted) or (right_begin < len(arr) and arr[left_end] > arr[right_begin]):
        left_end -= 1
        unsorted_begin -= 1
        
    while (right_begin >= 0 and arr[right_begin] < max_unsorted) or (left_end >=0 and arr[right_begin] < arr[left_end]):
        right_begin += 1
        unsorted_end += 1
        
    return unsorted_begin, unsorted_end
    
def find_unordered_subsequence2(arr):
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return 0, 0
        
		# traverse i forward from beginning of array until unsorted entry is found
        i = 0
        while arr[i+1] > arr[i]:
            i += 1
        # traverse j backwards from end of array until unsorted entry is found or it overlaps with ordered set
        j = len(arr) - 1
        while arr[j-1] < arr[j] and arr[j] > arr[i-1]:
            j -= 1
        
		# find min and max element between i and j (unordered set)
        maximum_mid = arr[i]
        minimum_mid = arr[i]
        for k in range(i, j+1):
            if arr[k] > maximum_mid:
                maximum_mid = arr[k]
            elif arr[k] < minimum_mid:
                minimum_mid = arr[k]
        
        # move left boundary of unordered set back until the last element of the left ordered set is less than minimum of unordered set      
        m = i - 1
        while m >= 0 and arr[m] > minimum_mid:
            m -= 1
        
        # move right boundary of unordered set forward until the first element of the right ordered set is greater than maximum of unordered set		
        n = j + 1
        while n < len(arr) and arr[n] < maximum_mid:
            n += 1
            
        return m + 1, n - 1
            
        
    
def main():
    #arr = [1, 4, 7, 6, 9, 3, 12, 18, 21, 24]
    #arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    arr = [19, 14, 12, 3, 2]
    
    #ret = find_unordered_subsequence(arr)
    #print ret
    #print arr[0:ret[0]] + sorted(arr[ret[0]:ret[1]+1]) + arr[ret[1]+1:]
    
    ret = find_unordered_subsequence2(arr)
    print ret
    print arr[0:ret[0]] + sorted(arr[ret[0]:ret[1]+1]) + arr[ret[1]+1:]

    
main()