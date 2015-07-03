# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 08:50:43 2014

@author: stree_001
"""
import time
import matplotlib.pyplot as pyplot
import random 

def merge(arr1, arr2):
    i1 = 0
    i2 = 0
    m_arr = []
    #count = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            m_arr.append(arr1[i1])
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            m_arr.append(arr2[i2])
            i2 += 1
            #count += 1
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
    
    return m_arr

def merge_sort(in_arr):
    if len(in_arr) < 2:
        return in_arr
    
    arr = in_arr

    m_left = merge_sort(arr[0:(len(arr)/2)])
    m_right = merge_sort(arr[(len(arr)/2):])
    merged = merge(m_left, m_right)
    return merged

def binary_search(arr, item, begin):
    mid = len(arr)/2
    if arr[mid] == item:
        return begin + mid
    elif item < arr[mid]:
        return binary_search(arr[0:mid], item, begin)
    else:
        return binary_search(arr[mid+1:], item, mid + 1)
        
def count_inversion2(arr):
    sorted_arr = merge_sort(arr)
    count = 0
    for idx in range(len(arr)):
        sorted_item_pos = binary_search(sorted_arr, arr[idx],0)
        #print arr[idx], idx, sorted_item_pos, count
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
    
def merge_count_inversions(arr1, arr2):
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
            # count remaining numbers in left array as inversions
            count += (len(arr1) - i1)
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

def count_inversion3(in_arr):
    if len(in_arr) < 2:
        return in_arr, 0
    
    arr = in_arr

    m_left, count_left = count_inversion3(arr[0:(len(arr)/2)])
    m_right, count_right = count_inversion3(arr[(len(arr)/2):])
    merged, count_merged = merge_count_inversions(m_left, m_right)
    return merged, count_left + count_right + count_merged

def run_trials(stop, increment):
    x = []
    y_1 = []
    y_2 = []
    y_3 = []

    for size in range(0, stop, increment):
        arr = [random.randint(-100,100) for _ in range(size)]
        x.append(size)
        
        start_count1 = time.time()
        count_inversion(arr)
        y_1.append(time.time() - start_count1)
        
        start_count2 = time.time()
        count_inversion2(arr)
        y_2.append(time.time() - start_count2)
        
        start_count3 = time.time()
        count_inversion3(arr)
        y_3.append(time.time() - start_count3)
        
        #start_qsort = time.time()
        #quick_sort(arr)
        #y_quick.append(time.time() - start_qsort)
    
    return x, y_1, y_2, y_3
    
def plot(x, y_1, y_2, y_3):
    pyplot.figure(1)
    pyplot.subplot(211)

    pyplot.plot(x, y_1, '-r', label="quadratic count inversions")
    pyplot.plot(x, y_2, '-b', label="merge sort then compare")
    pyplot.plot(x, y_3, '-g', label="enhanced merge sort")
    #pyplot.plot(x, y_quick, '-y', label="quick sort")
    
    pyplot.legend(loc='upper right')
    pyplot.axis([0, max(x), 0, max(max(y_1), max(y_2), max(y_3))])
    #pyplot.xscale('log')
    #pyplot.yscale('log')
    pyplot.xlabel('Items')
    pyplot.ylabel('Time')
    pyplot.title('Time for sort algs')
    #annotation = "maxi=", maxi
    #pyplot.annotate(s=annotation)
    pyplot.show()
    
def main():
    arr =  [2, 4, 1, 3, 5]
    arr = [1, 3, 5, 2, 4, 6]  
    arr = [2,7,8,3,4]
    print count_inversion(arr)
    #print merge_sort(arr)
    print count_inversion2(arr)
    print count_inversion3(arr)[1]
    #print inverts
    #print count
    x, y_1, y_2, y_3 = run_trials(3000, 50)
    plot(x, y_1, y_2, y_3)

main()