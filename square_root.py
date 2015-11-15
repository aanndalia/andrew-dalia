# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 12:26:25 2015

@author: stree_001
"""

def sqrt(n):
    c = 1.0
    tolerance = 0.0000001
    while ((c * c) < (n - tolerance)) or ((c * c) > (n + tolerance)):
        print "c", c
        c = (c + n/c) / 2
    return c
    
def main():
    print sqrt(100)
    print sqrt(2)
    
main()