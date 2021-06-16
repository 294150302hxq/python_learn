#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-06-16
# @Author : duliri_hxq

# 时间复杂度为O(n^2)，空间复杂度为O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        for i in range(len(nums)):
            temp_max = nums[i]
            sum_num = nums[i]
            for j in range(i+1,len(nums)):
                sum_num += nums[j]
                if sum_num>temp_max:
                    temp_max = sum_num
            if temp_max > max_sum:
                max_sum = temp_max
        return max_sum

    # 时间和空间复杂度均为O(n^2)，这个和上面基本一致，只是利用了存储好的计算值，意义不大
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        max_sum = nums[0]
        dp = [[nums[0]] * length for _ in range(length)]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j - 1] + nums[j]
                if dp[i][j] > max_sum:
                    max_sum = dp[i][j]
        return max_sum

    # 时间复杂度均为O(n)，空间复杂度为O(1)，在遍历数组过程中进行转移，每次记录的是到该值为止的最大子序列和
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        max_sum = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            pre = max(pre + nums[i], nums[i])
            if pre > max_sum:
                max_sum = pre
        return max_sum