'''
43. Multiply Strings
Solved
Medium
Topics
Companies
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''


def multiply(num1: str, num2: str) -> str:
    if not num1 or not num2:
        return ''

    multiplier = 1
    carry = 0
    res = 0
    for n2 in range(len(num2) - 1, -1, -1):
        mult = 1
        adder_row = 0
        carry = 0
        for n1 in range(len(num1) - 1, -1, -1):
            x = ord(num1[n1]) - ord('0')
            y = ord(num2[n2]) - ord('0')
            digit_res = (x * y + carry) * mult
            digit = digit_res // mult
            carry = digit_res % mult
            adder_row += digit * mult
            # print (x, y, digit_res, mult, digit, carry, adder_row)
            mult *= 10
        
        # print(res, adder_row, multiplier)
        res += adder_row * multiplier
        multiplier *= 10
    
    res = str(res)
    return res