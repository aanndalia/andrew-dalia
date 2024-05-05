def fourSum(nums: List[int], target: int) -> List[List[int]]:
    if not nums or len(nums) < 4:
        return []

    results = set()
    nums = sorted(nums)
    # print(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                # print(i, j, left, right, nums[i], nums[j], nums[left], nums[right])
                four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if four_sum == target:
                    results.add(tuple(sorted([nums[i], nums[j], nums[left], nums[right]])))
                    left += 1
                    right -= 1
                elif four_sum < target:
                    left += 1
                else:
                    right -= 1

    return list(results)
