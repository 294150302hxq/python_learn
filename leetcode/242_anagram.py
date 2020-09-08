#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/9/8
    @desc:
"""

def isAnagram1(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if sorted(s) == sorted(t):
        return True
    else:
        return False

def isAnagram2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_dict = {}
    for ch in s:
        if ch not in s_dict.keys():
            s_dict[ch] = 1
        else:
            s_dict[ch] += 1
    t_dict = {}
    for ch in t:
        if ch not in t_dict.keys():
            t_dict[ch] = 1
        else:
            t_dict[ch] += 1
    for k in s_dict.keys():
        if k not in t_dict.keys() or s_dict[k] != t_dict[k]:
            return False
    if len(s_dict.keys()) == len(t_dict.keys()):
        return True
    else:
        return False

# 同方法2比较的话没有用到更多的python方法
def isAnagram3(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_dict, t_dict = {}, {}
    for ch in s:
        s_dict[ch] = s_dict.get(ch, 0) + 1
    for ch in t:
        t_dict[ch] = t_dict.get(ch, 0) + 1
    return s_dict == t_dict