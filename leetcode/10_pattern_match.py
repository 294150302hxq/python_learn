#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/13
    @desc:
"""


class Solution(object):
    def isMatch(self, s, p):
        # 如果p为空了，s为空返回真，否则返回假
        if not p: return not s

        # 如何p不为空，那么只有当s不为空，且p的第一位和s的第一位匹配上才算是真，否则为假
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            # 优先级为and（>1个） or（0个）
            return (self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p))
        else:
            # 均往后走1位
            return first_match and self.isMatch(s[1:], p[1:])