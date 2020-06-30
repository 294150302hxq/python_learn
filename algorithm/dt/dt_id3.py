#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/3/16
    @desc:
"""
from math import log


# 信息熵计算
def get_info_entropy(data):
    data_size = len(data)
    if data_size > 0:
        # 统计有多少个类，每个类有多少
        label_size_dict = {}
        for item in data:
            label = item['label']
            if label in label_size_dict.keys():
                label_size_dict[label] += 1
            else:
                label_size_dict[label] = 1
        info_entropy = 0
        for label, size in label_size_dict.items():
            p = size*1.0/data_size
            info_entropy -= p*log(p, 2)
        return info_entropy
    else:
        return 0


# 计算信息增益
def get_gain(data_info, feature_list):
    for feat in feature_list:
        for item in data_info:
            pass

