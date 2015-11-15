def binary_search_rotated(arr, begin, end, target):
    print begin, end
    mid = (begin + end) / 2
    if arr[mid] == target:
        return mid
    
    if end <= begin:
        return -1
    
    if arr[begin] < arr[mid]:
        # left sorted
        if target < arr[mid] and target >= arr[begin]:
            # target possibly on left
            return binary_search_rotated(arr, begin, mid-1, target)
        else:
            # target possibly on right
            return binary_search_rotated(arr, mid+1, end, target)
            
    else:
        # right sorted
        if target > arr[mid] and target <= arr[end]:
            # target possible on right
            return binary_search_rotated(arr, mid+1, end, target)
        else:
            return binary_search_rotated(arr, begin, mid-1, target)


arr = [6,7,1,2,3,4,5]
target = 1
print binary_search_rotated(arr, 0, len(arr)-1, target)
