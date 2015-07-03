# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 07:21:50 2014

@author: stree_001
"""

def gen_all_permutations(s):
    s_len = len(s)
    if s_len < 2:
        return s
        
    gen_permutes = []
    for i in range(s_len):
        first = s[i]
        before = s[0:i]
        after = s[i+1:s_len]
        permutes = gen_all_permutations(before + after)
        for p in permutes:
            gen_permutes.append(first + p)
    
    return gen_permutes
    
def gen_all_combinations(s):
    return set(gen_all_permutations(s))
            
def main():
    print gen_all_permutations("hello")
    print len(gen_all_permutations("hello"))
    # cat -> cat, cta, act, atc, tca, tac
    print gen_all_permutations("cat")
    print gen_all_combinations("hello")
    print len(gen_all_combinations("hello"))
    print gen_all_combinations("hollo")
    print len(gen_all_combinations("hollo"))
    

main()