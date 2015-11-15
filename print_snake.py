# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 23:14:32 2015

@author: stree_001
"""

import math

def print_snake(mat, N):
    print math.ceil(N/2.0)
    for i in range(int(math.ceil(N/2.0))):
        first = i
        last = N-1-i
        for j in range(first, last):
            print mat[first][j],
        for j in range(first, last):
            print mat[j][last],
        for j in range(first, last):
            print mat[last][N-1-j],
        for j in range(first, last):
            print mat[N-1-j][first],
            
def main():
    mat = [[1,2,3], [4,5,6], [7,8,9]]
    print_snake(mat, 3)
    
main()