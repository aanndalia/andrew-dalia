# -*- coding: utf-8 -*-
"""
Created on Sun Feb 01 18:04:51 2015

@author: stree_001
"""
def dest_heuristic(word, dest):
    dist = 0
    for i in range(len(word)):
        if word[i] != dest[i]:
            dist += 1

def word_ladder(start, end, dictionary):
    

start = "hit"
end = "cog"
d = set(["hot","dot","dog","lot","log"])

print word_ladder(start, end, d)


