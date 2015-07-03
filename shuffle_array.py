# -*- coding: utf-8 -*-
"""
Created on Sat Nov 08 11:52:46 2014

@author: stree_001
"""
import random

# shuffle array
def shuffle_arr(arr):
    for i in range(1, len(arr)):
        rand = random.randint(0, i)
        tmp = arr[i]
        arr[i] = arr[rand]
        arr[rand] = tmp
    
def main():
    arr = [-2, -1, 0, 3, 5, 6, 7, 9, 13, 14]
    shuffle_arr(arr)
    print arr
    
main()