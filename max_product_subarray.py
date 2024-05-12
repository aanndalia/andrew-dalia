'''
152. Maximum Product Subarray
Solved
Medium
Topics
Companies
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

def maxProduct(nums: List[int]) -> int:
    product = 1
    max_left_cur_product = nums[0]
    max_right_cur_product = nums[-1]
    has_zero = False
    for i, num in enumerate(nums):
        if num == 0:
            has_zero = True
            product = 1
        else:
            product *= num
            max_left_cur_product = max(max_left_cur_product, product)

    rprod = 1
    for i in range(len(nums) - 1, -1, -1):
        # print(nums[i], rprod, max_right_cur_product)
        if nums[i] == 0:
            rprod = 1
        else:
            rprod *= nums[i]
            max_right_cur_product = max(max_right_cur_product, rprod)

    max_prod = max(max_left_cur_product, max_right_cur_product) 
    if has_zero:
        return max(max_prod, 0)
    
    return max_prod