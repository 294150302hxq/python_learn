#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/28
    @desc:
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head  or not head.next: return head
        a = head
        b = head.next
        c = ListNode()
        rs = c
        while a is not None and b is not None:
            a.next = b.next
            b.next = a
            c.next = b
            c = a
            a = a.next
            if a is not None:
                b = a.next
        return rs.next