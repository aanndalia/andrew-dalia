# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 21:45:41 2014

@author: stree_001
"""
import random
import time
import matplotlib.pyplot as pyplot

def selection_sort(arr):
    if len(arr) < 2:
        return arr
        
    new_arr = arr
    for i in range(len(new_arr)):
        minimum = new_arr[i]
        for j in range(i+1, len(new_arr)):
            if new_arr[j] < minimum:
                minimum = new_arr[j]
        new_arr[i] = minimum
    
    return new_arr
    
def insertion_sort(arr):
    if len(arr) < 2:
        return arr
        
    new_arr = arr
    for i in range(1, len(new_arr)):
        #print "new_arr", new_arr
        temp = new_arr[i]
        if temp < new_arr[i-1]:
            j = i
            while j > 0 and new_arr[j-1] > temp:
                new_arr[j] = new_arr[j-1]
                j -= 1
                
            new_arr[j] = temp
           
    return new_arr
                

def merge(arr1, arr2):
    i1 = 0
    i2 = 0
    m_arr = []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            m_arr.append(arr1[i1])
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            m_arr.append(arr2[i2])
            i2 += 1
        else:
            m_arr.append(arr1[i1])
            m_arr.append(arr2[i2])
            i1 += 1
            i2 += 1
    
    #if i1 < (len(arr1) - 1):
    while i1 < len(arr1):
        m_arr.append(arr1[i1])
        i1 += 1
    #elif i2 < (len(arr2) - 1):
    while i2 < len(arr2):
        m_arr.append(arr2[i2])
        i2 += 1
    
    #print "arr1", arr1
    #print "arr2", arr2
    #print "m_arr", m_arr
    return m_arr

def merge_sort(in_arr):
    if len(in_arr) < 2:
        return in_arr
    
    arr = in_arr
    #print "left", arr[0:(len(arr)/2)]
    #print "right", arr[(len(arr)/2):]
    m_left = merge_sort(arr[0:(len(arr)/2)])
    m_right = merge_sort(arr[(len(arr)/2):])
    return merge(m_left, m_right)
  
def run_trials(stop, increment):
    x = []
    y_merge = []
    y_insertion = []
    y_selection = []
    for size in range(0, stop, increment):
        arr = [random.randint(-100,100) for _ in range(size)]
        x.append(size)
        
        start_msort = time.time()
        merge_sort(arr)
        y_merge.append(time.time() - start_msort)
        
        start_isort = time.time()
        insertion_sort(arr)
        y_insertion.append(time.time() - start_isort)
        
        start_ssort = time.time()
        selection_sort(arr)
        y_selection.append(time.time() - start_ssort)
    
    return x, y_merge, y_insertion, y_selection
    
def plot(x, y_merge, y_insertion, y_selection):
    pyplot.figure(1)
    pyplot.subplot(211)
    
    pyplot.plot(x, y_merge, '-r', label="merge sort")
    pyplot.plot(x, y_insertion, '-b', label="insertion sort")
    pyplot.plot(x, y_selection, '-g', label="selection sort")
    
    pyplot.legend(loc='upper right')
    pyplot.axis([0, max(x), 0, max(max(y_merge), max(y_insertion), max(y_selection))])
    #pyplot.xscale('log')
    #pyplot.yscale('log')
    pyplot.xlabel('Items')
    pyplot.ylabel('Time')
    pyplot.title('Time for sort algs')
    #annotation = "maxi=", maxi
    #pyplot.annotate(s=annotation)
    pyplot.show()
  
def main():
    #arr = [8, -55, -20, 9, 0, 11, -13, 6, 14, 99, -2, 11]
    #print merge_sort(arr)
    #print insertion_sort(arr)
    
    arr2 = [random.randint(-100,100) for _ in range(10)]
    print "unsorted arr2", arr2
    print "merge sorted arr2", merge_sort(arr2)
    print "insertion sorted arr2", insertion_sort(arr2)
    print "selection sorted arr2", selection_sort(arr2)
    
    x, y_m, y_i, y_s = run_trials(1000, 50)
    plot(x, y_m, y_i, y_s)
    
    
main()