#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/20
    @desc:
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rs = {}
        for i in nums:
            if i in rs.keys():
                rs[i] = rs[i]+1
            else:
                rs[i] = 1
            if rs[i] > len(nums)//2:
                return i