# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 08:50:43 2014

@author: stree_001
"""

def merge(arr1, arr2):
    i1 = 0
    i2 = 0
    m_arr = []
    count = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            m_arr.append(arr1[i1])
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            m_arr.append(arr2[i2])
            i2 += 1
            count += 1
        else:
            m_arr.append(arr1[i1])
            m_arr.append(arr2[i2])
            i1 += 1
            i2 += 1
    
    while i1 < len(arr1):
        m_arr.append(arr1[i1])
        i1 += 1
        
    while i2 < len(arr2):
        m_arr.append(arr2[i2])
        i2 += 1
        #count += 1
    
    return m_arr, count

def merge_sort(in_arr):
    if len(in_arr) < 2:
        return in_arr, 0
    
    arr = in_arr

    m_left, count_left = merge_sort(arr[0:(len(arr)/2)])
    m_right, count_right = merge_sort(arr[(len(arr)/2):])
    merged, m_count = merge(m_left, m_right)
    return merged, count_left + m_count + count_right

def binary_search(arr, item, begin):
    mid = len(arr)/2
    if arr[mid] == item:
        return begin + mid
    elif item < arr[mid]:
        return binary_search(arr[0:mid], item, begin)
    else:
        return binary_search(arr[mid+1:], item, mid + 1)
        
def count_inversion2(arr):
    sorted_arr, rubbish = merge_sort(arr)
    count = 0
    for idx in range(len(arr)):
        sorted_item_pos = binary_search(sorted_arr, arr[idx],0)
        print arr[idx], idx, sorted_item_pos, count
        if idx < sorted_item_pos:
            count += (sorted_item_pos - idx)
            #del sorted_arr[sorted_item_pos]
            #del arr[idx]
            
    return count
    
def count_inversion(arr):
    if len(arr) < 2:
        return 0
    
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

def main():
    arr =  [2, 4, 1, 3, 5]
    arr = [1, 3, 5, 2, 4, 6]  
    arr = [2,7,8,3,4]
    #print count_inversion(arr)
    print merge_sort(arr)
    print count_inversion2(arr)
    #print inverts
    #print count

main()