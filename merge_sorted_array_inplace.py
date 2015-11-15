# 2 sorted arrays, a1 and a2, of lengths l1 and l2, respectively. 
# The array a2 has empty space at the end of length l1, 
# so it can hold all of the elements of a1 in addition to its own elements. 
# Merge a1 into a2 so that a2 will contain all the elements of a1 and a2 
# in sorted order
def merge(a1, a2):
    for i in range(len(a1)):
        if a1[i] == None:
            a1_len = i
            break
            
    merged_len = len(a1)
    a2_len = len(a2)
    
    i1 = a1_len - 1
    i2 = a2_len - 1
    i = merged_len - 1
    #print a1_len, a2_len, merged_len
    while i1 >= 0 and i2 >= 0:
        #print a1[i1], a2[i2], a1[i]
        if a1[i1] > a2[i2]:
            a1[i] = a1[i1]
            i -= 1
            i1 -= 1
        else:
            a1[i] = a2[i2]
            i -= 1
            i2 -= 1
            
    return a1
    
def main():
    a1 = [1, 5, 7, 9, None, None, None] 
    a2 = [2, 4, 8]
    print merge(a1, a2)

main()