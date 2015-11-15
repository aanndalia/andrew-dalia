# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 08:42:06 2014

@author: stree_001
"""

def trim_spaces(s):
    #begin = 0
    i = 0
    output = ""
    while i < len(s):
        if s[i] != " ":
            output = output + s[i]
            i += 1
        else:
            while s[i] == " " and i < len(s):
                i += 1
                
            output = output + " "
        #i += 1
        #print output
        
    return output
        
    
def main():
    s = "I   live   on     earth"
    print trim_spaces(s)
    
main()