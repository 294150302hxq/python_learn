#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/1/11
    @desc:
"""
mailto = ['cc', 'bbbb', 'afa', 'sss', 'bbbb', 'cc', 'shafa']
mailto.insert(2,'ff')
mailto.insert(2,'ff')
deli = set(['bbbb'])
print set(mailto) - deli
addr_to = list(set(mailto) - deli)
addr_to.sort(key = mailto.index)
print(addr_to)