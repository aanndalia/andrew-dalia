# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 08:01:57 2014

@author: stree_001
"""

import time
import matplotlib.pyplot as pyplot

# find the possible paths for a robot to move from 0,0 to X,Y given that it can
# only move down and right from the upper left corner
def move_paths2(x, y, X, Y):
    if X < 0:
        return [[]]
    if Y < 0:
        return [[]]
    
    if x > X: 
        return [[]]
    if y > Y:
        return [[]]
    
    paths = []
    
    if x+1 <= X:    
        paths_right = move_paths2(x+1, y, X, Y)
        for pr in paths_right:
            paths += [[x+1,y] + [pr]]
    else:
        paths += [[x+1, y]]
            
    if y+1 <= Y:
        paths_down = move_paths2(x, y+1, X, Y)
        for pd in paths_down:
            paths += [[x,y+1] + [pd]]
    else:
        paths += [[x, y+1]]
            
    return paths
    
def move_paths(x, y, X, Y, paths):
    if X < 0:
        return False
    if Y < 0:
        return False
        
    if X < x :
        return False
    if Y < y:
        return False
        
    if x < 0:
        return False
    if y < 0:
        return False
        
    point = (x,y)
    paths.append(point)
    
    if x == 0 and y == 0:
        print paths
        return True
    
    left_success = move_paths(x-1,y,X,Y,list(paths))
    up_success = move_paths(x,y-1,X,Y,list(paths))
    
    if left_success or up_success:
        return True
    else:
        return False
        
def move_paths_out(x, y, X, Y, current_path, paths, d):
    if X < 0:
        return False
    if Y < 0:
        return False
        
    if X < x :
        return False
    if Y < y:
        return False
        
    if x < 0:
        return False
    if y < 0:
        return False
        
    point = (x,y)
    current_path.append(point)
    
    if x == 0 and y == 0:
        #print current_path
        #print paths
        #d[point] = True
        paths.append(current_path)
        return True
        
    #if point in d:
        #if point == (0,0):
        #    print paths
        #print d
        #return d[point]
    
    left_success = move_paths_out(x-1,y,X,Y,list(current_path), paths, d)
    up_success = move_paths_out(x,y-1,X,Y,list(current_path), paths, d)
    
    if left_success or up_success:
        #d[point] = True
        return True
    else:
        #d[point] = False
        return False
        
def move_paths_dp(x, y, X, Y, current_path, paths, d):
    point = (x,y)
    if X < 0 or X < x or x < 0 or Y < 0 or Y < y or y < 0:
        d[point] = False
        return False
        
    current_path.append(point)
    
    if x == 0 and y == 0:
        #d[point] = True
        paths.append(current_path)
        return True
        
    if point in d:
        #if point == (0,0):
        #    print paths
        #print d
        return False
    
    left_success = move_paths_dp(x-1,y,X,Y,list(current_path), paths, d)
    up_success = move_paths_dp(x,y-1,X,Y,list(current_path), paths, d)
    
    if left_success or up_success:
        #d[point] = True
        return True
    else:
        d[point] = False
        return False
        
def run_trials(stop, increment):
    x = []
    y_recursive = []
    y_dp = []
    for n in range(1, stop, increment):
        for m in range(1, stop, increment):
            #arr = [random.randint(-100,100) for _ in range(size)]
            x.append(n + m)
        
            start_recursive = time.time()
            #move_paths_out(n)
            current_path = []
            paths = []
            d = {}
            move_paths_out(m,n,m,n,current_path,paths,d)
            y_recursive.append(time.time() - start_recursive)
        
            start_dp = time.time()
            current_path = []
            paths = []
            d = {}
            move_paths_dp(m,n,m,n,current_path,paths,d)
            y_dp.append(time.time() - start_dp)
    
    return x, y_recursive, y_dp
    
def plot(x, y_recursive, y_dp):
    pyplot.figure(1)
    pyplot.subplot(211)
    
    pyplot.plot(x, y_recursive, '-r', label="recursive")
    pyplot.plot(x, y_dp, '-b', label="dp")
    
    pyplot.legend(loc='upper right')
    pyplot.axis([0, max(x), 0, max(max(y_recursive), max(y_dp))])
    #pyplot.xscale('log')
    #pyplot.yscale('log')
    pyplot.xlabel('n')
    pyplot.ylabel('Time')
    pyplot.title('Time for step problem')
    #annotation = "maxi=", maxi
    #pyplot.annotate(s=annotation)
    pyplot.show()   
    
def main():
    #for path in move_paths2(0,0,1,2):
    #    print path
    #print
    
    move_paths(2,4,2,4,[])
    print
    current_path = []
    paths = []
    d = {}
    move_paths_out(3,5,3,5,current_path,paths,d)
    print len(paths)
    for p in paths:
        print p

    current_path = []
    paths = []
    d = {}
    move_paths_dp(2,4,2,4,current_path,paths,d)
    print len(paths)
    for p in paths:
        print p
        
    x, y_rec, y_dp = run_trials(5,1)
    plot(x, y_rec, y_dp)
        
main()