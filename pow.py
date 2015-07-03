# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:21:07 2015

@author: stree_001
"""

def pow(a, b):
    if b == 0:
        return 1
    
    if a == 0 or a == 1 or b == 1:
        return a
    
    half_pow = pow(a, b/2)
    
    if b % 2 == 0:
        return half_pow * half_pow
    else:
        return half_pow * half_pow*a
    
x = pow(2,31)
print x