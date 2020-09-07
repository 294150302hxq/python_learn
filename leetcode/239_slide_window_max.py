#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/9/7
    @desc:
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1 or not nums or len(nums) == 0: return nums
        rs,index_list = [],[]
        n = 0
        for i,num in enumerate(nums):
            n += 1
            while len(index_list)>0 and num>=nums[index_list[-1]]:
                index_list.pop()
            index_list.append(i)
            if n >= k:
                rs.append(nums[index_list[0]])
            if i - index_list[0] == k-1:
                index_list.pop(0)
        return rs

    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1 or not nums or len(nums) == 0: return nums
        rs,window = [], []
        for i,num in enumerate(nums):
            while i >= k and window[0] <= i-k:
                window.pop(0)
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                rs.append(nums[window[0]])
        return rs