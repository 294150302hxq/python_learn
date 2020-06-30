#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/6/28
    @desc:
"""

from collections import defaultdict


class Solution(object):
    # Brute Force
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Two-pass Hash Table
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        num_map = defaultdict(set)
        for i in range(length):
            num_map[nums[i]].add(i)
        for i in range(length):
            left = target - nums[i]
            if left in nums:
                rs = num_map[left] - set([i])
                if len(rs) > 0:
                    return [i,list(rs)[0]]

    # One-pass Hash Table
    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        num_map = defaultdict(list)
        for i in range(length):
            if i <> 0:
                left = target - nums[i]
                if left in num_map.keys():
                    return [num_map[left][0], i]
            num_map[nums[i]].append(i)
