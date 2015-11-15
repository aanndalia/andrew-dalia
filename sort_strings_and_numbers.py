# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 06:30:00 2014

@author: stree_001
"""

"""
Input:

car truck 8 4 bus 6 1

Output:

bus car 1 4 truck 6 8
"""

"""
Program to sort list of words and numbers
example above
"""

def sort_strings_and_numbers(arr):
    if len(arr) < 2:
        return arr
        
    type_arr = [arr[i].isdigit() for i in range(len(arr))] # True for numbers, False for strings
    arr_sorted = sorted(arr)
    output = ["" for _ in range(len(arr))]
    
    type_iter = 0
    sorting_strings = False
    #print arr_sorted
    for j in range(len(arr_sorted)):
        if sorting_strings == False and arr_sorted[j].isdigit() == False:
            sorting_strings = True
            type_iter = 0
            
        if sorting_strings == False:
            while type_arr[type_iter] == False:
                type_iter += 1
                #output.append(arr_sorted[j])
        else:
            while type_arr[type_iter] == True:
                type_iter += 1
                    
        output[type_iter] = arr_sorted[j]
        #output.append(arr_sorted[j])
        #print j, type_iter, output
        type_iter += 1
            
    return output
        
        
def main():
    print "car".isdigit()
    print "123".isdigit()
    arr = ["car", "truck", "8", "4", "bus", "6", "1"]
    print arr
    print sort_strings_and_numbers(arr)
    
main()