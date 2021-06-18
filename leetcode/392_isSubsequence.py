#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-06-18
# @Author : duliri_hxq


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        n = 0
        for ch in t:
            if ch == s[n]:
                n += 1
            if n == len(s):
                return True
        return False