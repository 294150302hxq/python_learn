#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-06-17
# @Author : duliri_hxq

class Solution(object):
    # 时间复杂度O(n^2)，空间复杂度O(1)，但是会有超时的问题存在
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        length = len(prices)
        for i in range(length):
            pre = 0
            for j in range(i,length):
                pre = max(prices[j]-prices[i],pre)
                if max_profit < pre:
                    max_profit = pre
        return max_profit

    # 时间复杂度O(n)，空间复杂度O(1)
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        length = len(prices)
        for i in range(length):
            max_profit = max(max_profit, prices[i]-min_price)
            if min_price > prices[i]:
                min_price = prices[i]
        return max_profit