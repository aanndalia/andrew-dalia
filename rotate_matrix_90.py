# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 00:42:37 2014

@author: stree_001
"""

def print_matrix(arr):
    for r in arr:
        for c in r:
            if c >= 10:
                print c,
            else:
                print "0" + str(c),
        print

def rotate_matrix_90(arr, N):
    for layer in range(0, N/2):
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            offset = i - first
            
            # save top element
            top = arr[first][i]
            
            # left to top (previous rhs is this lhs)
            arr[first][i] = arr[last-offset][first]
            
            # bottom to left (previous rhs is this lhs)
            arr[last-offset][first] = arr[last][last-offset]
            
            # right to bottom
            arr[last][last-offset] = arr[i][last]
            
            # top to right
            arr[i][last] = top
    
def main():
    arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    print_matrix(arr)
    print
    rotate_matrix_90(arr, 4)
    print_matrix(arr) 
    
main()