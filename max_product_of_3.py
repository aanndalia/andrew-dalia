# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 23:06:47 2014

@author: stree_001
"""

def max_product_of_3(arr):
    # Finds the maximum product of 3 integers in the array
    highest_positive1 = arr[0]
    highest_positive2 = arr[0]
    highest_positive3 = arr[0]
    
    lowest_negative1 = arr[0]
    lowest_negative2 = arr[0]
    lowest_negative3 = arr[0]
    
    for num in arr:
        if num > highest_positive1:
            highest_positive3 = highest_positive2
            highest_positive2 = highest_positive1
            highest_positive1 = num
        elif num > highest_positive2:
            highest_positive3 = highest_positive2
            highest_positive2 = num
        elif num > highest_positive3:
            highest_positive3 = num
        elif num < lowest_negative1:
            lowest_negative3 = lowest_negative2
            lowest_negative2 = lowest_negative1
            lowest_negative1 = num
        elif num < lowest_negative2:
            lowest_negative3 = lowest_negative2
            lowest_negative2 = num
        elif num < lowest_negative3:
            lowest_negative3 = num
            
    candidates = [highest_positive1 * highest_positive2 * highest_positive3, lowest_negative1 * lowest_negative2 * highest_positive1]
    return max(candidates)
    
def main():
    print max_product_of_3([-6, 4, 7, -3, 0, -1, 5, 1])
    
main()
        
            