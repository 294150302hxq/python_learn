#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/15
    @desc:
"""

class Solution(object):
    # Brute Force
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        max_water = 0
        for i in range(length-1):
            for j in range(i+1,length,1):
                max_water = max(max_water, min(height[i],height[j]) * (j-i))
        return max_water

    # increasing, already find the most of it, otherwise can't move it
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(height) - 1
        max_water = 0
        while a != b:
            max_water = max(max_water, (b - a) * min(height[a], height[b]))
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return max_water
