# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 14:51:28 2014

@author: stree_001
"""

#s1 = "OBFUSCATION"
#s2 = "eschew"
#s3 = "OBesFUScCheATIwON"

#s1 = "obfuscation"
#s2 = "eschew"
#s3 = "obesfusccheatiwon"

def shuffled_string_x(s1, s2, s, i, i1, i2):    
    while i < len(s):
        if s[i] == s[i1] and s[i] != s[i2]:
            i += 1
            i1 += 1
        elif s[i] != s[i1] and s[i] == s[i2]:
            i += 1
            i2 += 1
        elif s[i] == s[i1] and s[i] == s[i2]:
            shuffled_1 = shuffled_string(s1, s2, s, i+1, i1+1, i2)
            shuffled_2 = shuffled_string(s1,s2,s,i+1,i1, i2+1)
        else:
            return False
        
    return True
    
def shuffled_string(s1, s2, s, i, i1, i2, s_out): 
    #if i
    if i1 >= len(s1): 
        if s[i] != s2[i2]:
            return False
        else:
            if i == len(s) - 1:
                return True
            s_out.append(s2[i2].upper())
            return shuffled_string(s1, s2, s, i+1, i1, i2+1, s_out)
            
    if i2 >= len(s2): 
        if s[i] != s1[i1]:
            return False
        else:
            if i == len(s) - 1:
                return True
            s_out.append(s1[i1])
            return shuffled_string(s1, s2, s, i+1, i1+1, i2, s_out)
            
    print "s", s[i], "s1", s1[i1], "s2", s2[i2]    
    if s[i] == s1[i1] and s[i] != s2[i2]:
        s_out.append(s1[i1])
        return shuffled_string(s1, s2, s, i+1, i1+1, i2, s_out)
    elif s[i] == s2[i2] and s[i] != s1[i1]:
        s_out.append(s2[i2].upper())
        return shuffled_string(s1,s2,s, i+1, i1, i2+1, s_out)
    elif s[i] == s1[i1] and s[i] == s2[i2]:
        #s_out.append(s1[i1])
        #s1_out = list(s_out) + [s1[i1]]
        #s2_out = list(s_out) + [s2[i2].upper()]
        #shuffled_1 = shuffled_string(s1, s2, s, i+1, i1+1, i2, s1_out)
        #shuffled_2 = shuffled_string(s1,s2,s,i+1,i1, i2+1, s2_out)
        shuffled_1 = shuffled_string(s1, s2, s, i+1, i1+1, i2, list(s_out) + [s1[i1]])
        shuffled_2 = shuffled_string(s1,s2,s,i+1,i1, i2+1, list(s_out) + [s2[i2]])
        #if shuffled_1 or shuffled_2:
        #    return True
        if shuffled_1 == True:
            #s_out = s1_out
            return True
        elif shuffled_2 == True:
            #s_out = s2_out
            return True
        else:
            print "collision false"
            return False
    else:
        print "else False"
        return False
        
    print "End of fn"
        
def shuffled(s1, s2, s):
    if len(s) != len(s1) + len(s2):
        print "lengths don't sum up"
        return False
    
    s_out = []
    ret = shuffled_string(s1, s2, s, 0, 0, 0, s_out)
    return s_out, ret    
    
def main():
    s1 = "obfuscation"
    s2 = "eschew"
    s  = "obesfusccheatiwon"
    #s1 = "ab"
    #s2 = "bc"
    #s = "abbc"
    print shuffled(s1,s2,s)
    
main()
            
        