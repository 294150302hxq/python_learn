#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/23
    @desc:
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = ["(","[","{"]
        d = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0