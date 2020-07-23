#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/23
    @desc:
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
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
        if length == 1 or length == 0:
            return None
        if n == length:
            return head.next

        position = length - n + 1
        i = 0
        b = None
        while head is not None:
            i += 1
            if i == position and i == length:
                b.next = None
            elif i == position:
                head = head.next
                continue
            elif b is None:
                b = ListNode()
                a = b
                b.val = head.val
            else:
                b.next = head
                b = b.next
                b.val = head.val
            head = head.next
        return a

    def removeNthFromEnd1(self, head, n):
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

        if length == 1 or length == 0:
            return None
        if n == length:
            return head.next

        position = length - n + 1
        i = 0
        a = head
        while head is not None:
            i += 1
            if i == position - 1:
                head.next = head.next.next
            else:
                head = head.next
        return a