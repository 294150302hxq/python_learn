#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/22
    @desc:
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # O(n^3)
        rs = []
        if not digits: return rs
        ch_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for ch in ch_dict[digits[0]]:
            rs.append(ch)
        for i in range(1, len(digits)):
            new_rs = []
            for st in rs:
                for ch in ch_dict[digits[i]]:
                    new_rs.append(st + ch)
            rs = new_rs
        return rs