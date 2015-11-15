# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 10:41:55 2015

@author: stree_001
"""
def five_factors(x):
    count = 0
    while x > 1 and (x % 5) == 0:
        count += 1
        x = x / 5
        
    return count

def trailingZeroes(n):
        if n < 5:
            return 0
            
        count = 0    
        for i in range(5, n+1, 5):
            count += five_factors(i)
                    
        return count
        
for i in range(26):
    print i, trailingZeroes(i)
    
for i in range(26):
    print i, five_factors(i)
    
print trailingZeroes(25)
print trailingZeroes(125)
