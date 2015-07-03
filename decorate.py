# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:02:04 2015

@author: stree_001
"""

def add(a, b):
    return a + b
    
def sub(a,b):
    return a - b

# wrapper function that makes result 0 if it's less than 0
# this is the decorator
def wrapper(fn):
    def check(a, b):
        result = fn(a,b)
        if result < 0:
            return 0
        else:
            return result
            
    return check
    
@wrapper 
def add_dec(a, b):
    return a + b
 
@wrapper   
def sub_dec(a, b):
    return a - b
 
add_decorated_fn = wrapper(add)  
sub_decorated_fn = wrapper(sub)

print "manually decoration using higher-order functional programming"

print add_decorated_fn(1, 3)
print add_decorated_fn(1, -3)

print sub_decorated_fn(1, 3)
print sub_decorated_fn(1, -3)

print
print "using decorators"

print add_dec(1, 3)
print add_dec(1, -3)

print sub_dec(1, 3)
print sub_dec(1, -3)

print
print "no decoration"

print add(1, 3)
print add(1, -3)

print sub(1, 3)
print sub(1, -3)