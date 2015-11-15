# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 07:55:54 2015

@author: stree_001
"""

def longestPalindrome(s):
    if len(s) == 0:
        return ""
        
    if len(s) == 1:
        return s
        
    max_palindrome_length = 1
    max_palindrome = s[0]
    for i in range(0, len(s)):
        l = i-1
        r = i+1
        count = 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            print "odd", i, l, r, s[l], s[r]
            count += 2
            if count > max_palindrome_length:
                max_palindrome_length = count
                max_palindrome = s[l:r+1]
            r += 1
            l -= 1
        #print count    
        
            
        l = i
        r = i+1
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 2
            if count > max_palindrome_length:
                max_palindrome_length = count
                max_palindrome = s[l:r+1]
            r += 1
            l -= 1
            
    return max_palindrome
    
def main():
    s = "bab"
    print longestPalindrome(s)
    s = "b"
    print longestPalindrome(s)
    s = "bb"
    print longestPalindrome(s)
    
main()