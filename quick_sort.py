# -*- coding: utf-8 -*-

def calc_median(nums):
    return sorted(nums)[len(nums)/2]

def quick_sort(arr):
    print "arr", arr
    if len(arr) < 2:
        return arr
    
    if len(arr) == 2:
        if arr[0] <= arr[1]:
            return arr
        else:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            return arr
            
    part_arr = [arr[0], arr[len(arr)/2], arr[len(arr)-1]]
    median = calc_median(part_arr)

    left = []
    right = []
    equal = []
    for num in arr:
        if num < median:
            left.append(num)
        elif num == median:
            equal.append(num)
        else:
            right.append(num)
          
    lqs = quick_sort(left)
    rqs = quick_sort(right)
    return lqs + equal + rqs
        
def main():
    arr = [8, -55, -20, 9, 0, 11, -13, 6, 14, 99, -2, 11]
    #arr = [1,3,2]
    #arr = [4,2,7,6,3,2,10,9]
    print quick_sort(arr)
    
main()