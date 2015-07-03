# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:37:18 2015

@author: stree_001
"""

def spiral(mat):
    left = 0
    right = len(mat) - 1
    top = 0
    bottom = len(mat) - 1
    
    while((right > left) and (bottom > top)):
        # top
        for i in range(left, right + 1):
            print mat[top][i],
        top += 1
        
        # right
        for i in range(top, bottom + 1):
            print mat[i][right],
        right -= 1
        
        # bottom    
        for i in range(right, left - 1, -1):
            print mat[bottom][i],
        bottom -= 1
            
        # left
        for i in range(bottom, top - 1, -1):
            #print i, left
            print mat[i][left],
        left += 1
        
m = [[1,  2, 3, 4],
     [5,  6, 7, 8],
     [9, 10,11,12],
     [13,14,15,16]]
     
spiral(m)