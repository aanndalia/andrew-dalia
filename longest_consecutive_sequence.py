# -*- coding: utf-8 -*-
"""
Created on Sun Feb 01 16:11:13 2015

@author: stree_001
"""

def longestConsecutive(num):
    if len(num) == 0:
        return 0
        
    if len(num) == 1:
        return 1
        
    num_set = set(num)
    max_length = 1
    for i in range(len(num)):
        length = 1
        j = num[i] + 1
        while j in num_set:
            length += 1
            if length > max_length:
                max_length = length
            j += 1
    
    return max_length
    
def longestConsecutive2(num):
    if len(num) == 0:
        return 0
        
    if len(num) == 1:
        return 1
        
    d = {}
    for i in range(len(num)):
        if num[i] not in d:
            d[num[i]] = False
            
    max_length = 1
    for i in range(len(num)):
        j = num[i] - 1
        k = num[i] + 1
        count = 1
        while j in d and d[j] == False:
            d[j] = True
            j -= 1
            count += 1
        while k in d and d[k] == False:
            d[k] = True
            k += 1
            count += 1
            
        if count > max_length:
            max_length = count
    
    return max_length
    
print longestConsecutive([100, 4, 200, 1, 3, 2])

print longestConsecutive2([100, 4, 200, 1, 3, 2])