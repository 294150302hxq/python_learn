#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/20
    @desc:
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        rs = strs[0]
        for i in range(1, len(strs)):
            max_len = min(len(rs), len(strs[i]))
            if max_len == 0:
                return ""
            tmp = ''
            for j in range(max_len):
                if rs[j] == strs[i][j]:
                    tmp += rs[j]
                else:
                    break
            rs = tmp
        return rs