# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 00:15:02 2014

@author: stree_001
"""

#import fileinput

def path_sum_2_way(matrix, x, y, N, d, current_path, path_sum, path_sums):
    point = (x,y)
    current_path.append(point)
    path_sum = path_sum + matrix[x][y]
    if point == (N-1, N-1):
        #current_path.append(point)
        #path_sum = path_sum + matrix[x][y]
        path_sums.append(path_sum)
        return
        
    if x+1 < N:
        path_sum_2_way(matrix, x+1, y, N, d, list(current_path), path_sum, path_sums)
    if y+1 < N:
        path_sum_2_way(matrix, x, y+1, N, d, list(current_path), path_sum, path_sums)
        
    return
    
def path_sum_2_way_dp(matrix, x, y, N, d, current_path, path_sum, path_sums):
    point = (x,y)
    current_path.append(point)
    path_sum = path_sum + matrix[x][y]
    
    if point in d:
        if path_sum >= d[point]:
            return
        else:
            d[point] = path_sum
    else:
        d[point] = path_sum
        
    if point == (N-1, N-1):
        #current_path.append(point)
        #path_sum = path_sum + matrix[x][y]
        path_sums.append(path_sum)
        return
        
    if x+1 < N:
        path_sum_2_way(matrix, x+1, y, N, d, list(current_path), path_sum, path_sums)
    if y+1 < N:
        path_sum_2_way(matrix, x, y+1, N, d, list(current_path), path_sum, path_sums)
        
    return
    
def path_sum_2_way_dp2(matrix, x, y, N, d, path_sum, path_sums):
    point = (x,y)
    #current_path.append(point)
    path_sum = path_sum + matrix[x][y]
    
    if point in d:
        if path_sum >= d[point]:
            return
        else:
            d[point] = path_sum
    else:
        d[point] = path_sum
        
    if point == (N-1, N-1):
        #current_path.append(point)
        #path_sum = path_sum + matrix[x][y]
        path_sums.append(path_sum)
        return
        
    if x+1 < N:
        path_sum_2_way_dp2(matrix, x+1, y, N, d, path_sum, path_sums)
    if y+1 < N:
        path_sum_2_way_dp2(matrix, x, y+1, N, d, path_sum, path_sums)
        
    return
        
def min_path_sum_2_way(matrix, N):
    x = 0
    y = 0
    d = {}
    #current_path = []
    path_sum = 0
    path_sums = []
    path_sum_2_way_dp2(matrix, x, y, N, d, path_sum, path_sums)
    return min(path_sums)
    
def main():
    print "from test"
    matrix = [[2,7,5], [4,1,3], [8,9,6]]
    print matrix
    print len(matrix)
    path_sums = []
    path_sum_2_way(matrix, 0, 0, len(matrix), {}, [], 0, path_sums)
    print path_sums
    print min_path_sum_2_way(matrix, len(matrix))
    
    print "from file"
    matrix = []
    with open("data/p081_matrix.txt") as f:
        for line in f:
            l = line.rstrip()
            row = l.split(",")
            for r in range(len(row)):
                row[r] = int(row[r])
                
            matrix.append(row)
    
    print matrix
    print len(matrix)
    
    print min_path_sum_2_way(matrix, len(matrix))
    
main()