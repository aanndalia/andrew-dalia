# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 07:59:50 2014

@author: stree_001
"""

"""
Reverse the individual words of a string but not the string itself
"""

def reverse_word(s):
    s = list(s)
    for i in range(len(s)/2):
        temp = s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = temp
    
    s = ''.join(s)
    return s        

def reverse_words_of_string(s):
    output = []
    begin = 0
    i = 0
    while i < len(s):
        if s[i] == " ":
            output.append(reverse_word(s[begin:i]))
            begin = i + 1
        i += 1
    
    output.append(reverse_word(s[begin:i]))
    return ' '.join(output)
    
def main():
    s = "Hello I am the fish"
    print reverse_word(s)
    print reverse_words_of_string(s)
    
main()
    