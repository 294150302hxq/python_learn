#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/7/30
    @desc:
"""

class Solution(object):
    def detectCycle(self, head):
        pointer1 = head
        pointer2 = head
        while pointer1 is not None and pointer2 is not None:
            try:
                pointer1, pointer2 = pointer1.next, pointer2.next.next
            except Exception as e:
                return None
            if pointer1 == pointer2:
                pointer2 = head
                while pointer1 != pointer2:
                    pointer1, pointer2 = pointer1.next, pointer2.next
                return pointer2
        return None