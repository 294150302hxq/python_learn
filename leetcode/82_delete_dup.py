#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/12/20
    @desc:
"""


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        first_head = head
        node_list = []
        flag = False
        while first_head.next:
            if first_head.val != first_head.next.val and not flag:
                node_list.append(first_head.val)
            if first_head.val != first_head.next.val and flag:
                flag = False
            if first_head.val == first_head.next.val:
                flag = True
            first_head = first_head.next
        if not flag:
            node_list.append(first_head.val)
        rs = None
        head = None
        for val in node_list:
            if not head:
                head = ListNode(val)
                rs = head
            else:
                head.next = ListNode(val)
                head = head.next
        return rs