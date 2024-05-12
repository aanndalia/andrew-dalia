'''
50. Pow(x, n)
Solved
Medium
Topics
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''

def myPow(x: float, n: int) -> float:
    # x^n = x^(n/2)*x^(n/2)
    if n == 0:
        return 1
    if x == 0:
        return 0       
    if x == 1:
        return 1       
    if n == 1:
        return x
    
    base_neg = x < 0
    if base_neg:
        x = abs(x)
    
    exp_neg = n < 0
    if exp_neg:
        n = abs(n)

    half_pow = myPow(x, n // 2)
    res = half_pow * half_pow if n % 2 == 0 else half_pow * half_pow * x

    if base_neg and n % 2 != 0:
        res = -res
    if exp_neg:
        res = 1 / res

    return res