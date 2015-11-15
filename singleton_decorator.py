# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 08:49:45 2015

@author: stree_001
"""

def singleton(cls):
    """
    singleton is a decorator function
    """
    instances = {}
    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return instance
    
class A(object):
    pass

@singleton 
class B(object):
    pass

@singleton 
class C(object):
    pass

def main():
    a1 = A()
    a2 = A()
    print a1
    print a2
    
    b1 = B()
    b2 = B()
    print b1
    print b2
    
    c1 = C()
    c2 = C()
    print c1
    print c2
    
    b3 = B()
    c3 = C()
    print b3
    print c3
    
main()
    
            

        