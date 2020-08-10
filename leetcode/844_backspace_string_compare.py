#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/8/4
    @desc:
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S_stack = []
        T_stack = []
        for ch in S:
            if ch == '#':
                if len(S_stack)>0:
                    S_stack.pop()
            else:
                S_stack.append(ch)
        for ch in T:
            if ch == '#' :
                if len(T_stack)>0:
                    T_stack.pop()
            else:
                T_stack.append(ch)
        print(S_stack,T_stack)
        while len(S_stack) != 0 and len(T_stack) != 0:
            if S_stack.pop() != T_stack.pop():
                return False
        if len(S_stack)>0 or len(T_stack)>0:
            return False
        return True
