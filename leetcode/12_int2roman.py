#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/17
    @desc:
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII',
                    8: 'VIII', 9: 'IX', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                    40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        fen_mu = [1000, 900, 500, 400, 100, 90, 50, 40, 10]
        rs = ''
        for i in fen_mu:
            n = num / i
            num = num % i
            if n == 0:
                continue
            elif n == 1:
                rs += num_dict[i]
            else:
                rs += num_dict[i]*n
        if num != 0:
            rs += num_dict[num]
        return rs