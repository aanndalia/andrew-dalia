def threeSumClosest(nums: List[int], target: int) -> int:
    if not nums:
        return 0

    if len(nums) < 3:
        return 0

    if len(nums) == 3:
        return sum(nums)

    nums = sorted(nums)

    closest_sum = min(sum(nums[:3]), sum(nums[-3:]))

    print(nums)
    for i, num in enumerate(nums):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            # print(i, left, right, num, nums[left], nums[right], closest_sum)
            three_sum = num + nums[left] + nums[right]
            if three_sum == target:
                return three_sum
            elif three_sum < target:
                left += 1
            else:
                right -= 1

            if abs(target - three_sum) < abs(target - closest_sum):
                closest_sum = three_sum

    return closest_sum

