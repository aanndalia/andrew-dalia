# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:53:47 2015

@author: stree_001
"""

# gets all pairings of parens for given number of open paren
# http://www.codeskulptor.org/#user39_zeanaYuH5y_0.py

def get_pairings(num_parens, left_remain, right_remain, current_order, solutions):
    if num_parens < 1:
        return None
    
    if num_parens == 1:
        current_order = ["(", ")"]
        solutions.append(["(", ")"])
        return
    
    if left_remain == 0 and right_remain == 0:
        solutions.append(current_order)
        return
        
    if left_remain == 0:
        current_order.append(")")
        get_pairings(num_parens, left_remain, right_remain - 1, current_order, solutions)
        return
    
    if right_remain < left_remain:
        return
    
    get_pairings(num_parens, left_remain, right_remain - 1, current_order + [")"], solutions)
    get_pairings(num_parens, left_remain - 1, right_remain, current_order + ["("], solutions)
    
    return
    

def main():
    num_parens = 3
    left_remain = num_parens
    right_remain = num_parens
    current_order = []
    solutions = []
    get_pairings(num_parens, left_remain, right_remain, current_order, solutions)
    print solutions
    for s in solutions:
        print "".join(s)
    
main()