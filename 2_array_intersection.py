# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:36:03 2015

@author: stree_001
"""

def two_array_intersect(arr1, arr2):
    if len(arr1) < 1:
        return None
        
    if len(arr2) < 1:
        return None
        
    i1 = 0
    i2 = 0
    output = []
    
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            i1 += 1
        elif arr1[i1] == arr2[i2]:
            output.append(arr1[i1])
            i1 += 1
            i2 += 1
        else:
            i2 += 1
            
    return output
    
def main():
    arr1 = [-3,1,4,7]
    arr2 = [-1,0,1,3,4]
    print two_array_intersect(arr1, arr2)

main()