def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    k = 2
    buy_at_transaction = [float('inf') for _ in range(k)]
    sell_at_transaction = [0 for _ in range(k)]
    for i, price in enumerate(prices):
        for t in range(k):
            sell_at_prev_transaction = sell_at_transaction[t - 1] if t - 1 >= 0 else 0
            buy_at_transaction[t] = min(buy_at_transaction[t], price - sell_at_prev_transaction)
            sell_at_transaction[t] = max(sell_at_transaction[t], price - buy_at_transaction[t])

    return sell_at_transaction[-1]
