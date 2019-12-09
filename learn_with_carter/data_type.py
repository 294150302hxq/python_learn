#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2019/12/4
    @desc:
"""

# int 2 float
print float(2)

# float 2 int，向下取整
print int(2.3)
print int(2.9)

# str 2 float，但是小数型str不能转int，如果需要可以先转float再转int
print float('2.3') # int('2.3')会报错
print int('3')

# homework 3
print int(13.2+0.5)
print int(13.7+0.5)