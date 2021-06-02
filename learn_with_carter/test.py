#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/1/11
    @desc:
"""


def decorator(func):
    def wrapper(*args, **kargs):
        print('begin call')
        rs = func(*args, **kargs)
        print('end call')
        return rs
    return wrapper


@decorator
def test():
    print(2+3)
    pass


test()



