# -*- coding: utf-8 -*-
"""
Created on Sat Nov 08 11:18:52 2014

@author: stree_001
"""

import random

# find all pairs of integers in an array that sum to a target value
def pair_sums(arr, target):
    num_counts = {}
    output = [] 
    complements = set([]) # all opposites to items, used to avoid duplicates
    for num in arr:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
            
    for rep_num in num_counts.keys():
        if ((target - rep_num) in num_counts) and ((target - rep_num) not in complements):
            for _ in xrange(num_counts[target - rep_num]):
                output.append((rep_num, target - rep_num))
            complements.add(rep_num)
        
    
    return output

def main():
    arr = [-2, -1, 0, 3, 5, 6, 7, 9, 13, 14]
    random.shuffle(arr)
    print arr
    print pair_sums(arr, 8)
    
main()