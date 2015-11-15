# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:00:25 2015

@author: stree_001
"""

arr = [4,2,8,6]

# maps each element in the array to new value using lambda
arr2 = map(lambda x: x ** 2, arr)
print arr2

# filters elements in the array that don't satisfy lambda condition
arr3 = filter(lambda x: x < 5, arr)
print arr3

# returns single number corresponding to lambda running between each
# element in sequence 
# [4,2,8,6] -> [4+2,8,6] -> [6+8,6] -> [14+6] -> [20]
arr4 = reduce(lambda x, y: x + y, arr)
print arr4