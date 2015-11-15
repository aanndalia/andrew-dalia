# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 07:44:35 2015

@author: stree_001
"""

class MinStack:
    def __init__(self):
        self.s = []
        self.smin = []
        
    def push(self, x):
        self.s.append(x)
        if len(self.smin) == 0 or x < self.smin[-1]:
            self.smin.append(x)
            
    def pop(self):
        if len(self.s) == 0:
            return None
            
        x = self.s.pop()
        if x == self.smin[-1]:
            self.smin.pop()
            
        return x
        
    def Min(self):
        if len(self.smin) == 0:
            return None
            
        return self.smin[-1]
        
    def print_stack(self):
        print self.s
        
    def print_min_stack(self):
        print self.smin
            
def main():
    s = MinStack()
    s.push(4)
    s.push(3)
    s.push(1)
    print "stack"
    s.print_stack()
    print s.Min()
    s.pop()
    print s.Min()
    s.push(6)
    s.push(2)
    print s.Min()
    s.pop()
    print s.Min()
    s.pop()
    print s.Min()
    s.pop()
    print s.Min()
    s.pop()
    print s.Min()
    s.pop()
    print s.Min()
    
main()
    
        