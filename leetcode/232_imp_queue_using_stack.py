#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/8/10
    @desc:
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2.pop()
        else:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2[len(self.stack2)-1]
        else:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[len(self.stack2)-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) + len(self.stack2)>0:
            return False
        else:
            return True