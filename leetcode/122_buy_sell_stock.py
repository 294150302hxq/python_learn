#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/21
    @desc:
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > pre_price:
                profit += prices[i] - pre_price
            pre_price = prices[i]
        return profit