'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


def permuteUnique(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    # permutations_set = set()
    memo = {}

    def recurse(num_list):
        if not num_list:
            return []

        if len(num_list) == 1:
            return [num_list]

        key = tuple(num_list)
        if key in memo:
            return memo[key]

        permutations_list = []
        for i in range(len(num_list)):
            first = num_list[i]
            rest = num_list[0:i] + num_list[i + 1:]
            rest_permutes = recurse(rest)
            for permute in rest_permutes:
                cur_permute = [first] + permute
                permutations_list.append(cur_permute)

        memo[key] = permutations_list
        return permutations_list

    all_permutations = recurse(nums)
    permutations_set = set([tuple(p) for p in all_permutations])
    return list(permutations_set)