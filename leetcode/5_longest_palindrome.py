#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/2
    @desc:
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if not s or length == 1 or length == 0:return s
        for i in range(length, 0, -1):
            n = 0
            while n+i <= length:
                sub_str = s[n:n+i]
                sub_str_re = sub_str[::-1]
                if sub_str_re == sub_str:
                    return sub_str
                n += 1