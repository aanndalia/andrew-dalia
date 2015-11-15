# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 18:23:19 2015

@author: stree_001
"""

def max_loss(prices):
    if len(prices) == 0:
        return None
    if len(prices) == 1:
        return 0, 0, prices[0], prices[0], 0
    
    buy_ind = 0
    sell_ind = 0
    max_loss = 0
    max_ind = 0
    min_ind = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[max_ind]:
            max_ind = i
        elif prices[i] < prices[min_ind]:
            min_ind = i
            loss = abs(prices[min_ind] - prices[max_ind])
            if loss > max_loss:
                buy_ind = max_ind
                sell_ind = min_ind
                max_loss = loss
    
    return buy_ind, sell_ind, prices[buy_ind], prices[sell_ind], max_loss
    
def main():
    prices = [20,50,75,15,125]
    print max_loss(prices)
    
main()