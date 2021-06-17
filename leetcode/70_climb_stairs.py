#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-06-17
# @Author : duliri_hxq


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        n1 = 1
        n2 = 2
        for i in range(n-2):
            n1, n2 = n2, n1+n2
        return n2