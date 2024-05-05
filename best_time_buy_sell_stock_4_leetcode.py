'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and
sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.7

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''


# side 1 is buy and -1 is sell
def recursive_max_profit(prices, remaining_sells, side, idx):
    if idx >= len(prices):
        return 0

    if remaining_sells < 1:
        return 0

    if side == 1:
        # buy
        take_action_profit = -prices[idx] + recursive_max_profit(prices, remaining_sells, -side, idx + 1)
        no_action_profit = recursive_max_profit(prices, remaining_sells, side, idx + 1)
        return max(take_action_profit, no_action_profit)
    else:
        # sell
        take_action_profit = prices[idx] + recursive_max_profit(prices, remaining_sells - 1, -side, idx + 1)
        no_action_profit = recursive_max_profit(prices, remaining_sells, side, idx + 1)
        return max(take_action_profit, no_action_profit)


def recursive_max_profit_memo(prices, remaining_sells, side, idx, memo_map):
    if idx >= len(prices):
        return 0

    if remaining_sells < 1:
        return 0

    memo_key = (remaining_sells, side, idx)
    if memo_key in memo_map:
        return memo_map[memo_key]

    if side == 1:
        # buy
        take_action_profit = -prices[idx] + recursive_max_profit_memo(prices, remaining_sells, -side, idx + 1, memo_map)
        no_action_profit = recursive_max_profit_memo(prices, remaining_sells, side, idx + 1, memo_map)
        max_prof = max(take_action_profit, no_action_profit)
    else:
        # sell
        take_action_profit = prices[idx] + recursive_max_profit_memo(prices, remaining_sells - 1, -side, idx + 1, memo_map)
        no_action_profit = recursive_max_profit_memo(prices, remaining_sells, side, idx + 1, memo_map)
        max_prof = max(take_action_profit, no_action_profit)

    memo_map[memo_key] = max_prof
    return max_prof


def max_profit(prices, k):
    if not prices or len(prices) < 2:
        return 0

    if not k:
        return 0

    # return recursive_max_profit(prices, k, 1, 0)
    return recursive_max_profit_memo(prices, k, 1, 0, {})


def main():
    # prices = [3, 2, 6, 5, 0, 3]
    prices = [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72,
              15, 11, 94]
    k = 2
    res = max_profit(prices, k)
    print(res)


main()
