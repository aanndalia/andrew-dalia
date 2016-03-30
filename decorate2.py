# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 06:39:15 2016

@author: stree_001
"""

def positiveCheck(fn):
    def checkAndCall(*args, **kwargs):
        res = fn(*args, **kwargs)
        if res < 0:
            return 0
        return res
    return checkAndCall
    
@positiveCheck
def add(a,b,c):
    return a + b + c

@positiveCheck    
def multiply(x,y):
    return x*y
    
def main():
    print add(1,2,3)
    print add(1,-2,-3)
    print multiply(1,2)
    print multiply(-1,2)
    
main()