# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 09:23:18 2016

@author: stree_001
"""

def permutes(arr):
    if len(arr) < 2:
        return [arr]
    
    allPermutes = []
    for i in range(len(arr)):
        first = [arr[i]]
        rest = arr[:i] + arr[i+1:]
        restPermutes = permutes(rest)
        for p in restPermutes:
            allPermutes.append(first + p)
            
    return allPermutes

def permutesDP(arr, cache={}):
    if len(arr) < 2:
        return [arr]
    
    if tuple(arr) in cache:
        return cache[tuple(arr)]
    
    allPermutes = []
    for i in range(len(arr)):
        first = [arr[i]]
        rest = arr[:i] + arr[i+1:]
        restPermutes = permutesDP(rest, cache)
        for p in restPermutes:
            #print first, p
            allPermutes.append(first + p)
    
    
    cache[tuple(arr)] = allPermutes
    return allPermutes


def permute(s):
    if len(s) < 2:
        return s
    
    permutations = []
    for i in range(len(s)):
        rest = s.split(s[i])
        rest_str = ''.join(rest)
        s_permutes = permute(rest_str)
        for p in s_permutes:
            permutations.append(s[i] + p)
            
    return permutations

arr = [1,2,3,4,5,6,7,8,9]
res = permutes(arr)
#for r in res:
#    print r
    
print

res = permutesDP(arr)
#for r in res:
#    print r

print
    
s = "bear"
x = permute(s)
print x
print len(x)