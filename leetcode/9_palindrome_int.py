#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/9
    @desc:
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        origin = x
        reverse = 0
        n = 1
        while x != 0:
            reverse = reverse*10 + x%10
            x = int(x/10)
            n += 1
        if reverse == origin:
            return True
        else:
            return False