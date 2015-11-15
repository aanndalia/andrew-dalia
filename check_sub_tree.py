# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:48:50 2015

@author: stree_001
"""

def is_sub_tree(big_root, small_root):
    if big_root == None and small_root == None:
        return True
    
    if big_root == None or small_root == None:
        return False
        
    return check_subtree(big_root, small_root)
    
def check_subtree(big_start, small_root):
    if big_start == None:
        return False
        
    if big_start.data == small_root.data:
        if match_tree(big_start, small_root):
            return True
    
    if check_subtree(big_start.left, small_root) or check_subtree(big_start.right, small_root):
        return True
        
    return False
    
def match_tree(big_subroot, small_subroot):
    if big_subroot == None and small_subroot == None:
        return True
        
    if big_subroot == None or small_subroot == None:
        return False
        
    if big_subroot.data != small_subroot.data:
        return False
        
    return match_tree(big_subroot.left, small_subroot.left) and match_tree(big_subroot.right, small_subroot.right)
    