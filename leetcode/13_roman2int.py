#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/17
    @desc:
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        RIMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rs = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and RIMap[s[i]] < RIMap[s[i + 1]]:
                rs += RIMap[s[i + 1]] - RIMap[s[i]]
                i += 2
            else:
                rs += RIMap[s[i]]
                i += 1
        return rs