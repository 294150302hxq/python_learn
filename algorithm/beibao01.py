#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/1/20
    @desc:
"""

# 0-1背包问题，要么选，要么不选，递归法
def ks(i, c):
    if (i == 0) | (c == 0):
        # 初识化
        result = 0
    elif ws[i] > c:
        # 装不下
        result = ks(i-1, c)
    else:
        # 装得下，要考虑是不是最优
        tmp1 = ks(i-1, c)
        tmp2 = ks(i-1, c-ws[i])+vs[i]
        result = max(tmp1, tmp2)
    return result


vs = [0,2,4,3,7]
ws = [0,2,3,5,5]
result = ks(4,10)
print(result)
