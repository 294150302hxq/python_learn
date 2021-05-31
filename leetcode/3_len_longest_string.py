#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/6/29
    @desc:
"""


class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        length =  len(s)
        max_rs = 0
        for i in range(length):
            rs = [s[i]]
            for j in range(i+1,length):
                if s[j] not in rs:
                    rs.append(s[j])
                else:
                    break
            if len(rs) > max_rs:
                max_rs = len(rs)
            if (length - i) < max_rs:
                return max_rs
        return max_rs

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        rs = []
        max_rs = 0
        for i in range(length):
            if s[i] not in rs:
                rs.append(s[i])
                max_rs = max(len(rs), max_rs)
            else:
                index = rs.index(s[i])
                rs = rs[index + 1:]
                rs.append(s[i])
        return max_rs