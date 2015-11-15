# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 10:20:39 2014

@author: stree_001
"""

def sum_up_to_n(n):
    sums = []
    for i in range(1, n):
        sums.append((i, n - i))
    return sums

def all_sums_up_to_n(n):
    if n == 2:
        return [(1, 1)]
    if n == 1:
        return [1]
        
    sums = []
    for i in range(1, n):
        #first_term = i
        rec_sums = all_sums_up_to_n(n - i)
        print "i", i, "rec_sums", rec_sums
        for s in rec_sums:
            temp_sums = []
            for num in s:
                temp_sums.append(num)
            sums.append([i] + temp_sums)
            
    return sums
    
def main():
    print sum_up_to_n(3)
    print sum_up_to_n(12)
    print all_sums_up_to_n(3)
    
main()