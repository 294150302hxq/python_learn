#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/6
    @desc:
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < numRows or not s or numRows == 1: return s
        rs = [''] * numRows
        add = 1
        pointer = 0
        for i in s:
            rs[pointer] += i
            if add == 1:
                pointer += 1
            else:
                pointer -= 1
            if pointer == numRows - 1:
                add = 0
            if pointer == 0:
                add = 1
        return ''.join(rs)
