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
    #cache = {}
    for i in range(5, n+1, 5):
        #print i, cache
        factors = five_factors(i)
        #cache[i] = factors
        count += factors
                    
    return count
    
def trailingZeroes2(n):
    if n < 5:
        return 0
           
    count = 0   
    for i in range(5, n+1, 5):
        x = i
        while x > 1:
            count += 1
            x = x / 5
                    
    return count
    
def trailingZeroes3(n):
    res = 0
    while n > 0:
        n = int(n/5) 
        res += n 
    return res
        
#for i in range(26):
#    print i, trailingZeroes(i)
    
#for i in range(26):
#    print i, five_factors(i)
    
print trailingZeroes(25)

x = 5*5*5
print x, trailingZeroes(x)

for i in range(26):
    print i, trailingZeroes3(i)
    
print trailingZeroes3(100)
