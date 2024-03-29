#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/12/27
    @desc:
"""


def quick_sort(num_list, i, j):
    if i >= j:
        return
    privot = num_list[i]
    left = i
    right = j
    while left < right:
        while left < right and num_list[right] >= privot:
            right -= 1
        num_list[left] = num_list[right]
        while left < right and num_list[left] <= privot:
            left += 1
        num_list[right] = num_list[left]
    num_list[right] = privot
    quick_sort(num_list, i, right - 1)
    quick_sort(num_list, right + 1, j)


def quick_sort1(num_list):
    if len(num_list) < 2:
        return num_list
    else:
        privot = num_list[0]
        less = [i for i in num_list[1:] if i <= privot]
        greater = [i for i in num_list[1:] if i > privot]
        return quick_sort1(less) + [privot] + quick_sort1(greater)


if __name__ == '__main__':
    a = [3,2,1,5,6,4]
    quick_sort(a, 0, len(a)-1)
    print(a)
    a = [3, 2, 1, 5, 6, 4]
    print(quick_sort1(a))