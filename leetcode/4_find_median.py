#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/1
    @desc:
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        left = ((l1+l2)/2 if (l1+l2)%2 == 0 else int((l1+l2)/2+1))
        right = int((l1+l2)/2+1)
        i = 0
        j = 0
        n = 0
        left_num = 0
        right_num = 0
        while i < l1 or j<l2:
            if (i<l1 and j<l2 and nums1[i] <= nums2[j]) or (j >= l2):
                n += 1
                if left == n:
                    left_num = nums1[i]
                if right == n:
                    right_num = nums1[i]
                    return (left_num+right_num)*1.0/2
                i += 1
            else:
                n += 1
                if left == n:
                    left_num = nums2[j]
                if right == n:
                    right_num = nums2[j]
                    return (left_num+right_num)*1.0/2
                j += 1