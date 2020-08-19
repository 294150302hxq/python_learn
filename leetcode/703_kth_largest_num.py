#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/8/19
    @desc:
"""
import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]

    def add1(self, val):
        """
           :type val: int
           :rtype: int
           """
        self.nums.append(val)
        self.nums.sort()
        self.nums = self.nums[len(self.nums) - self.k:]
        return self.nums[0]


class KthLargest1(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        ## 小顶堆建堆
        heapq.heapify(self.nums)
        ## 调整到k的大小
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
