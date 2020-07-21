#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/21
    @desc:
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n^3)
        if len(nums) < 3: return None
        nums.sort()
        length = len(nums)
        gap = abs(target - nums[0] - nums[1] - nums[2])
        rs = nums[0] + nums[1] + nums[2]
        for i in range(0,length-2):
            for j in range(i+1,length-1):
                for r in range(j+1,length):
                    new_gap = abs(target - nums[i] - nums[j] - nums[r])
                    if new_gap < gap:
                        rs = nums[i] + nums[j] + nums[r]
                        gap = new_gap
        return rs

    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n^2)
        nums.sort()
        length = len(nums)
        rs = nums[0] + nums[1] + nums[2]
        gap = abs(target - rs)
        for i in range(0, len(nums) - 2):
            l, r = i + 1, length - 1
            if i > 0 and nums[i] == nums[i - 1]: continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return total
                if gap > abs(target - total):
                    gap = abs(target - total)
                    rs = total
        return rs