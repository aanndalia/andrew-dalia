# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 02:00:45 2015

@author: stree_001
"""

def min_edit_distance(source, dest):
    source_len = len(source)
    dest_len = len(dest)
    matrix = [[0 for _ in range(dest_len + 1)] for _ in range(source_len + 1)]
    
    for j in range(dest_len + 1):
        matrix[0][j] = j
        
    for i in range(source_len + 1):
        matrix[i][0] = i
        
    for i in range(1, source_len + 1):
        source_char = source[i-1]
        for j in range(1, dest_len + 1):
            dest_char = dest[j-1]
            if source_char == dest_char:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min([matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]]) + 1
    
    for m in matrix:
        print m
        
    return matrix[source_len][dest_len]
    
print min_edit_distance("kitten", "sitting")