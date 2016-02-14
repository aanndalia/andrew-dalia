# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 23:39:59 2016

@author: stree_001
"""

def longestMonotonicallyIncreasingSubsequence(sequence):
    length = len(sequence)
    longestEndingAtIdx = [1] * length
    
    #lisAtEnding = [[sequence[0]] * length]
    
    
    for i in range(1, length):
        for j in range(0, i):
            if sequence[i] > sequence[j] and longestEndingAtIdx[i] < longestEndingAtIdx[j] + 1:
                longestEndingAtIdx[i] = longestEndingAtIdx[j] + 1
            
    longestIncreasingSubsequenceLength = max(longestEndingAtIdx)
    return longestIncreasingSubsequenceLength

def main():
    #sequence = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
    sequence = [10, 22, 9, 33, 21, 50, 41, 60]
    print longestMonotonicallyIncreasingSubsequence(sequence)
    
main()