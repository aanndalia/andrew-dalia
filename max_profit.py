# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 22:34:33 2014

@author: stree_001
"""
import matplotlib.pyplot as pyplot
#import math
import random
import time

# O(n^2) time O(1) space
def max_profit(arr):
    max_profit = arr[0]
    #cur_profit = 0
    buy_ind = 0
    sell_ind = 0
    buy = arr[0]
    sell = arr[0]
    arr_len = len(arr)
    for b_ind in range(1, arr_len):
        for s_ind in range(b_ind + 1, arr_len):
            if arr[s_ind] - arr[b_ind] > max_profit:
                max_profit = arr[s_ind] - arr[b_ind]
                sell = arr[s_ind]
                buy = arr[b_ind]
                buy_ind = b_ind
                sell_ind = s_ind
    
    return (sell_ind, buy_ind, sell, buy, max_profit)
    
# O(n) time O(1) space
def max_profit2(arr):
    if len(arr) < 2:
        return 0
    
    best_profit = 0
    cheapest = arr[0]
    cheapest_ind = 0
    sell_price = arr[0]
    buy_price = arr[0]
    buy_ind = 0
    sell_ind = 0
    
    for i in range(1, len(arr)):
        if arr[i] < cheapest:
            cheapest = arr[i]
            cheapest_ind = i
            
        if arr[i] - cheapest > best_profit:
            best_profit = arr[i] - cheapest
            sell_price = arr[i]
            buy_price = cheapest
            buy_ind = cheapest_ind
            sell_ind = i
            
    return (sell_ind, buy_ind, sell_price, buy_price, best_profit)

def run_trials(stop, increment):
    x = []
    p1 = []
    p2 = []
    #y_selection = []
    #y_quick = []
    for size in range(100, stop, increment):
        arr = [random.randint(0,100) for _ in range(size)]
        x.append(size)
        
        start_p1 = time.time()
        max_profit(arr)
        p1.append(time.time() - start_p1)
        
        start_p2 = time.time()
        max_profit2(arr)
        p2.append(time.time() - start_p2)
        
        #start_ssort = time.time()
        #selection_sort(arr)
        #y_selection.append(time.time() - start_ssort)
        
        #start_qsort = time.time()
        #quick_sort(arr)
        #y_quick.append(time.time() - start_qsort)
    
    return x, p1, p2
    
def plot(x, p1, p2):
    pyplot.figure(1)
    pyplot.subplot(211)
    
    pyplot.plot(x, p1, '-r', label="naive approach")
    pyplot.plot(x, p2, '-b', label="dynamic programming")
    #pyplot.plot(x, y_selection, '-g', label="selection sort")
    #pyplot.plot(x, y_quick, '-y', label="quick sort")
    
    pyplot.legend(loc='upper right')
    pyplot.axis([0, max(x), 0, max(max(p1), max(p1))])
    #pyplot.xscale('log')
    #pyplot.yscale('log')
    pyplot.xlabel('Items')
    pyplot.ylabel('Time')
    pyplot.title('Time for finding max profit algs')
    #annotation = "maxi=", maxi
    #pyplot.annotate(s=annotation)
    pyplot.show()

def main():
    print max_profit([50, 150, 25, 60, 10, 40, 130, 30])
    print max_profit2([50, 150, 25, 60, 10, 40, 130, 30])
    
    test_arr = [random.randint(0,100) for _ in range(20)]
    print test_arr
    print max_profit2(test_arr)
    
    x, p1, p2 = run_trials(1000, 10)
    plot(x, p1, p2)
    
main()