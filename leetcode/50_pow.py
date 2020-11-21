#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/20
    @desc:
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if x == 0:
        #     return 0
        # if n < 0:
        #     x = 1/x
        #     n = abs(n)
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return x
        # if n % 2 == 0:
        #     return self.myPow(x,n//2)*self.myPow(x,n//2)
        # else:
        #     return self.myPow(x,n//2)*self.myPow(x,n//2)*x
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        if n % 2:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n/2)