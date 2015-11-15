# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 08:19:54 2014

@author: stree_001
"""

s = [3, 5, 1, 4, 2]

def sort_stack(s):
    s2 = []
    while len(s) > 0:
        tmp = s.pop()
        while len(s2) > 0 and s2[-1] > tmp:
            s.append(s2.pop())
        s2.append(tmp)
    return s2
    
print sort_stack(s)
        
