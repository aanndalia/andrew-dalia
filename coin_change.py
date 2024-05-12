'''
322. Coin Change
Solved
Medium
Topics
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''

def coinChange(coins: List[int], amount: int) -> int:
    # Bottom up DP
    if not coins:
        return 0

    if not amount:
        return 0

    n = len(coins)

    # dp[i] is the min coins to make the remaining amount i
    dp = [0] + [float('inf')] * amount
    for amt_remain in range(1, amount + 1):
        for coin in coins:
            if amt_remain - coin >= 0:
                dp[amt_remain] = min(dp[amt_remain], dp[amt_remain - coin] + 1)
    
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


def coinChangeRecursive(coins: List[int], amount: int) -> int:
    if not coins:
        return 0

    if not amount:
        return 0

    min_coins_used_for_amount = float('inf')
    sum_coins_to_min_coins_used_map = {}
    def coin_change(coins_used, sum_coins):
        nonlocal min_coins_used_for_amount
        nonlocal sum_coins_to_min_coins_used_map
        if sum_coins == amount:
            min_coins_used_for_amount = min(min_coins_used_for_amount, len(coins_used))
            return
        
        if sum_coins > amount:
            return
        
        if sum_coins in sum_coins_to_min_coins_used_map and len(coins_used) >= sum_coins_to_min_coins_used_map[sum_coins]:
            return

        for coin in coins:
            coin_change(coins_used + [coin], sum_coins + coin)
        
        sum_coins_to_min_coins_used_map[sum_coins] = len(coins_used)

    coins = sorted(coins, reverse=True)
    coin_change([], 0)
    if min_coins_used_for_amount == float('inf'):
        return -1
    
    return min_coins_used_for_amount