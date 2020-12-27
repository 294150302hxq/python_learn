#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/12/27
    @desc:
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quick_sort(nums, 0, len(nums) - 1, k)
        return nums[k - 1]

    def quick_sort(self, num_list, i, j, k):
        if i >= j:
            return
        privot = num_list[i]
        left = i
        right = j
        while left < right:
            while left < right and num_list[right] <= privot:
                right -= 1
            num_list[left] = num_list[right]
            while left < right and num_list[left] >= privot:
                left += 1
            num_list[right] = num_list[left]
        num_list[right] = privot
        if right == k - 1:
            return
        elif right > k - 1:
            self.quick_sort(num_list, i, right - 1, k)
        else:
            self.quick_sort(num_list, right + 1, j, k)