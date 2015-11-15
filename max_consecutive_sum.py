# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 22:48:44 2014

@author: stree_001
"""
import time
import random
import matplotlib.pyplot as pyplot

def max_consecutive_sum(arr):
    max_sum = arr[0]
    for i in range(len(arr)):
        loop_sum = arr[i]
        for j in range(i+1, len(arr)):
            loop_sum += arr[j]
            if loop_sum > max_sum:
                max_sum = loop_sum
    return max_sum
    
def max_consecutive_sum_2(arr):
    #max_sum = arr[0]
    consecutive_sum = 0
    groups = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            consecutive_sum += arr[i]
        else:
            if consecutive_sum != 0:
                groups.append(consecutive_sum)
            groups.append(arr[i])
            consecutive_sum = 0
    #print consecutive_sums_groups
    
    j = 0
    max_sum = 0
    while j < len(groups):
        pair_sum = groups[j] + groups[j+1]
        if pair_sum > 0:
            max_sum += pair_sum
        else:
            j += 2
        
def max_consecutive_sum_3(arr):
    max_sum = arr[0]
    for i in range(len(arr)):
        loop_sum = arr[i]
        for j in range(i+1, len(arr)):
            loop_sum += arr[j]
            if loop_sum > max_sum:
                max_sum = loop_sum
            elif loop_sum < 0:
                break
    return max_sum
    
def max_consecutive_sum_4(arr):
    max_sum = arr[0]
    current_sum = 0
    for i in range(len(arr)):
        if current_sum <= 0:
            current_sum = arr[i]
        else:
            current_sum += arr[i]
            
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum
    
def main():
    #arr = [1, -2, 3, 10, -4, 7, 2, -5]
    arr = [random.randint(-1000,1000) for r in xrange(10000)]
    print arr[0:10]

    increment = 500
    items = 1000
    maxi = 5000
    items_data = []
    time1 = []
    time3 = []
    time4 = []
    while items < maxi:
        #print items,
        items_data.append(items)
        start1 = time.time()
        max_consecutive_sum(arr[0:items])
        time1.append(time.time() - start1)
    
        start3 = time.time()
        max_consecutive_sum_3(arr[0:items])
        time3.append(time.time() - start3)
        
        start4 = time.time()
        max_consecutive_sum_4(arr[0:items])
        time4.append(time.time() - start4)
        
        items += increment
        
    #pyplot.figure(1)
    pyplot.figure(1)
    pyplot.subplot(211)
    #pyplot.plot(x[0:100], y[0:100])
    print items_data
    print time1
    print time3
    print time4
    pyplot.plot(items_data, time1, '-r', label="time1" + str(len(time1)))
    pyplot.plot(items_data, time3, '-b', label="time3")
    pyplot.plot(items_data, time4, '-g', label="time4")
    #pyplot.plot(range(N+1), upa_resilience, '-g', label="UPA")
    
    pyplot.legend(loc='upper right')
    pyplot.axis([0,maxi,0,max(time1)])
    #pyplot.xscale('log')
    #pyplot.yscale('log')
    pyplot.xlabel('Items')
    pyplot.ylabel('Time')
    pyplot.title('Time for maximum subsequence algs')
    #annotation = "maxi=", maxi
    #pyplot.annotate(s=annotation)
    pyplot.show()
    
main()

