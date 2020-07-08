#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/8
    @desc:
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        n = 0
        while n < len(str):
            if str[n] != ' ':
                break
            n += 1
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        flag = 1
        if n == len(str):
            return 0
        elif str[n] in nums:
            flag = 1
        elif str[n] == '+':
            flag = 1
            n += 1
        elif str[n] == '-':
            flag = -1
            n += 1
        else:
            return 0

        # 去0
        while n < len(str):
            if (str[n]) != '0':
                break
            n += 1

        rs = ''
        while n < len(str) and str[n] in nums:
            rs += str[n]
            n += 1
        if len(rs) == 0: return 0
        if (len(rs) > 10 and flag == 1) or (flag == 1 and '0' * (10 - len(rs)) + rs > '2147483647'):
            return max_int
        elif (len(rs) > 10 and flag == -1) or (flag == -1 and '0' * (10 - len(rs)) + rs > '2147483647'):
            return min_int
        else:
            return flag * int(rs)