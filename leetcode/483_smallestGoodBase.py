#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-06-18
# @Author : duliri_hxq

import math


class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        max_len = math.log(n)/math.log(2)
        for length in range(int(max_len), 1, -1):
            k = int(math.pow(n, 1.0/length))
            total = 1
            tmp = 1
            for i in range(1, length+1):
                tmp *= k
                total += tmp
            if total == n:
                return str(k)
        return str(n-1)