# Given three arrays sorted in non-decreasing order, 
# print all common elements in these arrays

def find_common_elements(arr1, arr2, arr3):
    i1 = i2 = i3 = 0
    output = []
    while i1 < len(arr1) and i2 < len(arr2) and i3 < len(arr3):
        if (arr1[i1] == arr2[i2]) and (arr1[i1] == arr3[i3]):
            output.append(arr1[i1])
            i1 += 1
            i2 += 1
            i3 += 1
        else:
            if (arr1[i1] <= arr2[i2]) and (arr1[i1] <= arr3[i3]):
                i1 += 1
            elif (arr2[i2] <= arr1[i1]) and (arr2[i2] <= arr3[i3]):
                i2 += 1
            elif (arr3[i3] <= arr1[i1]) and (arr3[i3] <= arr2[i2]):
                i3 += 1
                
    return output

def main():
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    print find_common_elements(arr1, arr2, arr3)
    
    arr1 = [1, 5, 5]
    arr2 = [3, 4, 5, 5, 10]
    arr3 = [5, 5, 10, 20]
    print find_common_elements(arr1, arr2, arr3)
    
main()