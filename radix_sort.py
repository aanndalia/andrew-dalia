# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 07:46:58 2014

@author: stree_001
"""

def radix_sort(s, size):
    num_strings = len(s)
    LETTERS = 26
    ASCII_UPPER_CASE_CONVERSION = 65

    for d in range(size - 1, -1, -1):
        buckets = [[] for _ in range(LETTERS)]
        for n in range(num_strings):
            letter_bucket = ord(s[n][d]) - ASCII_UPPER_CASE_CONVERSION
            buckets[letter_bucket].append(s[n]) 
        s = [buckets[i][j] for i in range(LETTERS) for j in range(len(buckets[i]))]
        
    return s
            
def main():
    strings = ["COW", "DOG", "SEA", "ROW", "RUG", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"]
    print radix_sort(strings, 3)
    
main()