#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-04-11
# @Author : duliri_hxq


def find_smallest(arr):
    smallest_item = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_item:
            smallest_item = arr[i]
            smallest_index = i
    return smallest_index


def select_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(find_smallest(arr)))
    return new_arr

print(select_sort([1,4,5,3,2]))

