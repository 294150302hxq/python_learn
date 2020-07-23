#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/23
    @desc:
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None: return l2
        if l2 is None: return l1

        a = None
        b = None
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                if a is None:
                    a = ListNode(l1.val)
                    b = a
                else:
                    a.next = ListNode(l1.val)
                    a = a.next
                l1 = l1.next
            else:
                if a is None:
                    a = ListNode(l2.val)
                    b = a
                else:
                    a.next = ListNode(l2.val)
                    a = a.next
                l2 = l2.next
        if l1 is not None:
            a.next = l1
        if l2 is not None:
            a.next = l2
        return b