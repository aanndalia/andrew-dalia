def quickselect_median(nums):
    if not nums:
        return None

    n = len(nums)
    if n < 2:
        return nums[0]

    if n % 2 == 0:
        return (quickselect(nums, n / 2 - 1) + quickselect(nums, n / 2)) / 2.0
    else:
        return quickselect(nums, n // 2)


def quickselect(nums, idx):
    print(nums)
    if not nums:
        return None

    if len(nums) == 1:
        return nums[0]

    if len(nums) < 3:
        pivot = nums[0]
    else:
        pivot = sorted(nums[0:3])[1]

    left_slice = [num for num in nums if num < pivot]
    right_slice = [num for num in nums if num > pivot]
    equal_slice = [num for num in nums if num == pivot]

    if idx < len(left_slice):
        return quickselect(left_slice, idx)
    elif idx < len(left_slice) + len(equal_slice):
        return pivot
    else:
        return quickselect(right_slice, idx - len(equal_slice) - len(left_slice))


def main():
    nums = [9,1,0,2,3,4,6,8,7,10,5]
    res = quickselect_median(nums)
    return res


main()