#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/5/19
    @desc:
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    length = 0
    a = head
    while a is not None:
        length += 1
        a = a.next
    # 当只有一个的时候，则直接返回None
    if length == 1:
        return None
    position = length - n + 1
    b = ListNode()
    a = b
    i = 0
    while head is not None:
        i += 1
        if i == position:
            head = head.next
            continue
        elif i == position and position == length:
            b = None
            head = head.next
        else:
            b.val = head.val
            b.next = head.next
            b = b.next
            head = head.next
    return a