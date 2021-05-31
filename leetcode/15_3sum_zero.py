#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/21
    @desc:
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() #排序
        length = len(nums)
        rs = []
        for i in range(0,length-2):
            if nums[i] > 0:
                break
            # 跳过重复
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, length-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    rs.append([nums[i], nums[l], nums[r]])
                    # 跳过重复
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return rs