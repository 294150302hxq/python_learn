#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/1/11
    @desc:
"""


def max_num(rs, i, num, all_keys, all_stock_dicts, purchase_limit_dicts):
    key = all_keys[i - 1]
    print(i,num)
    if rs[i][num] != 0:
        return rs[i][num]
    max_n = 0
    if (num == 0) | (i == 0):
        max_n = 0
    else:
        k = 0
        while (k <= num) & (k <= all_stock_dicts[key]):
            tmp = 0
            if k >= purchase_limit_dicts[key]:
                tmp = max_num(rs, i - 1, num - k, all_keys, all_stock_dicts, purchase_limit_dicts) + k
            else:
                tmp = max_num(rs, i - 1, num, all_keys, all_stock_dicts, purchase_limit_dicts)
            if tmp > max_n:
                max_n = tmp
            k += 1
    rs[i][num] = max_n
    return max_n


min_dict = {"1": 4, "2": 6, "3": 4}
max_dict = {"1": 7, "2": 6, "3": 7}
num = 9
rs = []
for i in range(len(min_dict) + 1):
    rs.append([])
    for j in range(num + 1):
        rs[i].append(0)
all_keys = list(min_dict.keys())
print all_keys
max_num(rs, len(min_dict), num, all_keys, max_dict, min_dict)
print rs