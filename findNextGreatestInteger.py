def findNextGreatest(x):
    digits = list(str(x))
    print digits
    i = len(digits) - 1
    while i > 0 and digits[i] <= digits[i-1]:
        print digits[i], digits[i-1]
        i -= 1
        
    if i == 0:
        return x
       
    j = i
    while j < len(digits) and digits[j] > digits[i-1]:
        j += 1
        
    swapIdx = j - 1
    
    #print i, j, swapIdx
    
    temp = digits[swapIdx]
    digits[swapIdx] = digits[i-1]
    digits[i-1] = temp
    backSorted = sorted(digits[i:])
    nextGreatest = digits[:i] + backSorted
    return int(''.join(nextGreatest))

def main():
    x = 16329722
    print findNextGreatest(x)
    
main()