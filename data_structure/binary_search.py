#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-04-11
# @Author : duliri_hxq

def binary_search(arr, target):
    """
    the precondition of binary search is that the list is ordered
    time complexity: O(logn)
    space comlexity: O(n)
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

print(binary_search([1,3,5,9], 5))
print(binary_search([1,3,5,9], 6))