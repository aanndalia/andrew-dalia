'''
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0
    for num in nums:
        # if num is not the start of a sequence, skip it
        if num - 1 in num_set:
            continue

        seq_len = 1
        next_num = num + 1
        while next_num in num_set:
            seq_len += 1
            next_num += 1

        longest = max(longest, seq_len)

    return longest


def longestConsecutive2(self, nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    num_to_consec_list = {}
    visited = set()
    for num in nums:
        if num not in num_to_consec_list:
            num_to_consec_list[num] = [1]
            visited.add(num)

        cur_num = num - 1
        while cur_num in num_set and cur_num not in visited:
            num_to_consec_list[num] = [num_to_consec_list[num][0] + 1]
            num_to_consec_list[cur_num] = num_to_consec_list[num]
            visited.add(cur_num)
            cur_num -= 1

        cur_num = num + 1
        while cur_num in num_set and cur_num not in visited:
            num_to_consec_list[num] = [num_to_consec_list[num][0] + 1]
            num_to_consec_list[cur_num] = num_to_consec_list[num]
            visited.add(cur_num)
            cur_num += 1

    longest = 1
    for lst in num_to_consec_list.values():
        longest = max(longest, lst[0])

    return longest
