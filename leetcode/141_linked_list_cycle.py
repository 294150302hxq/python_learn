#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/30
    @desc:
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        pointer1 = head
        pointer2 = head
        while pointer1 is not None and pointer2 is not None:
            pointer1 = pointer1.next
            try:
                pointer2 = pointer2.next.next
            except Exception as e:
                return False
            if pointer1 == pointer2:
                return True
        return False