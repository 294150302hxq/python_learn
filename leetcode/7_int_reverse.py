#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/8
    @desc:
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2**31-1
        min_int = -2**31
        if x == 0: return 0
        sign = (-1 if x < 0 else 1)
        int_str = str(x*sign)
        int_str = int_str[::-1]
        # 去 0
        i = 0
        while i< len(int_str) and int_str[i] == '0':
            i += 1
        rs = 0
        length = len(int_str)
        while i< length:
            rs += int(int_str[i])*10**(length-i-1)
            i += 1
        if sign*rs >max_int or sign*rs<min_int:
            return 0
        return sign*rs