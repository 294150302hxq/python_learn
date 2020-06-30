#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/6/28
    @desc:
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rs = ListNode()
        n = 1
        up = 0
        rs_head = rs
        while (l1 is not None) & (l2 is not None):
            new_val = l1.val + l2.val + up
            up = int(new_val / 10)
            left = new_val % 10
            if n == 1:
                rs.val = left
                n += 1
                l1 = l1.next
                l2 = l2.next
            else:
                rs.next = ListNode(val=left)
                rs = rs.next
                l1 = l1.next
                l2 = l2.next

        while l1 is not None:
            new_val = l1.val + up
            up = int(new_val / 10)
            left = new_val % 10
            rs.next = ListNode(val=left)
            rs = rs.next
            l1 = l1.next

        while l2 is not None:
            new_val = l2.val + up
            up = int(new_val / 10)
            left = new_val % 10
            rs.next = ListNode(val=left)
            rs = rs.next
            l2 = l2.next

        if up > 0:
            rs.next = ListNode(val=up)

        return rs_head

    # consider the situation together
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rs = ListNode(0)
        up = 0
        rs_head = rs
        while (l1 is not None) | (l2 is not None):
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            new_val = val1 + val2 + up
            up = int(new_val / 10)
            left = new_val % 10
            rs.next = ListNode(val=left)
            rs = rs.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        if up > 0:
            rs.next = ListNode(val=up)

        return rs_head.next # this is a trick
