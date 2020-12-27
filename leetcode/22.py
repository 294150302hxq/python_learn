#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/12/2
    @desc:
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self._gen(0, 0, n, '')
        return self.result

    def _gen(self, left_used, right_used, n, one_rs):
        if left_used == n and right_used == n:
            self.result.append(one_rs)
            return
        if left_used < n:
            self._gen(left_used + 1, right_used, n, one_rs + '(')
        if left_used > right_used:
            self._gen(left_used, right_used + 1, n, one_rs + ')')