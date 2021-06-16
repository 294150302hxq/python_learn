#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/2
    @desc:
"""

class Solution(object):
    # 时间复杂度为O(n^2)，空间复杂度为O(n)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if not s or length == 1 or length == 0: return s
        for i in range(length, 0, -1):
            n = 0
            while n+i <= length:
                sub_str = s[n:n+i]
                sub_str_re = sub_str[::-1]
                if sub_str_re == sub_str:
                    return sub_str
                n += 1

    # 使用动态规划进行求解，转移方程为dp[i][j] = dp[i+1][j-1] & s[i] == s[j]
    # 时间和空间复杂度均为O(n^2)
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        max_len = 1
        begin = 0
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                # 边界条件
                if (j == i) or (j - i == 1 and s[i] == s[j]):
                    dp[i][j] = True
                # 状态转移
                if i < length - 1 and s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                # 记录转移过程中，最大的回文
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]