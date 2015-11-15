# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 08:15:56 2014

@author: stree_001
"""

import random
import time
import matplotlib.pyplot as pyplot

def all_steps_to_n(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    #if n == 2:
    #    return [[1,1],[0,2],[2,0]]
        
    one_step = [1] + all_steps_to_n(n-1)
    two_step = [2] + all_steps_to_n(n-2)
    
    if n > 2:
        three_step = [3] + all_steps_to_n(n-3)
    else:
        three_step = []
    
    return [one_step, two_step, three_step]
    
def all_steps_to_n_2(n, output):
    if n == 0:
        output.append([])
        return
    if n == 1:
        output.append([1])
        return
    #if n == 2:
    #    return [[1,1],[0,2],[2,0]]
        
    #one_step = [1] + step for step in all_steps_to_n(n-1)
    #two_step = [2] + all_steps_to_n(n-2)
    one_steps = []
    two_steps = []
    three_steps = []
    out = []
    #for step in all_steps_to_n_2(n-1, output):
    #    one_steps.append([1] + step)
        
    #for step in all_steps_to_n_2(n-2, list(output)):
    #    two_steps.append([2] + step)
    all_steps_to_n_2(n-1, out)
    for step in out:
        one_steps.append([1] + step)
    
    out = []    
    all_steps_to_n_2(n-2, out)
    for step in out:
        two_steps.append([2] + step)
        
    if n > 2:
        out = []
        all_steps_to_n_2(n-3, out)
        for step in out:
            three_steps.append([3] + step)
    
    for step in one_steps:
        output.append(step)
        
    for step in two_steps:
        output.append(step)
        
    for step in three_steps:
        output.append(step)
        
def all_steps_to_n_3(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    
    one_steps = []
    two_steps = []
    three_steps = []
    
    for step in all_steps_to_n_3(n-1):
        one_steps.append([1] + step)
     
    for step in all_steps_to_n_3(n-2):
        two_steps.append([2] + step)
        
    if n > 2:
        for step in all_steps_to_n_3(n-3):
            three_steps.append([3] + step)
    
    return one_steps + two_steps + three_steps
    
def all_steps_to_n_dp(n, d):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
        
    if n in d:
        return d[n]
    
    one_steps = []
    two_steps = []
    three_steps = []
    
    for step in all_steps_to_n_dp(n-1, d):
        one_steps.append([1] + step)
     
    for step in all_steps_to_n_dp(n-2, d):
        two_steps.append([2] + step)
        
    if n > 2:
        for step in all_steps_to_n_dp(n-3, d):
            three_steps.append([3] + step)
    
    steps = one_steps + two_steps + three_steps
    d[n] = steps
    return steps

def run_trials(stop, increment):
    x = []
    y_recursive = []
    y_dp = []
    for n in range(0, stop, increment):
        #arr = [random.randint(-100,100) for _ in range(size)]
        x.append(n)
        
        start_recursive = time.time()
        all_steps_to_n_3(n)
        y_recursive.append(time.time() - start_recursive)
        
        start_dp = time.time()
        all_steps_to_n_dp(n, {})
        y_dp.append(time.time() - start_dp)
    
    return x, y_recursive, y_dp
    
def plot(x, y_recursive, y_dp):
    pyplot.figure(1)
    pyplot.subplot(211)
    
    pyplot.plot(x, y_recursive, '-r', label="recursive")
    pyplot.plot(x, y_dp, '-b', label="dp")
    
    pyplot.legend(loc='upper right')
    pyplot.axis([0, max(x), 0, max(max(y_recursive), max(y_dp))])
    #pyplot.xscale('log')
    #pyplot.yscale('log')
    pyplot.xlabel('n')
    pyplot.ylabel('Time')
    pyplot.title('Time for step problem')
    #annotation = "maxi=", maxi
    #pyplot.annotate(s=annotation)
    pyplot.show()    
     
def main():
    n = 5
    print all_steps_to_n(n)
    
    output = []
    print all_steps_to_n_2(n, output)
    print output
    print len(output)
    n3_output = all_steps_to_n_3(n)
    #print output
    print n3_output
    print len(n3_output)
    dp_output = all_steps_to_n_dp(n, {})
    #print output
    print dp_output
    print len(dp_output)
    
    start_n3 = time.time()
    all_steps_to_n_3(23)
    print time.time() - start_n3
    
    start_d = time.time()
    all_steps_to_n_dp(23, {})
    print time.time() - start_d
    
    #x, y_recursive, y_dp = run_trials(n, 1)
    #plot(x, y_recursive, y_dp)
    
main()