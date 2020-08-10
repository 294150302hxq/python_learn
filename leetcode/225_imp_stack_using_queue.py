#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/8/10
    @desc:
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue1)==1:
            return self.queue1.pop(0)
        elif len(self.queue1)>1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.queue1)==1:
            return self.queue1[0]
        elif len(self.queue1)>1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1[0]
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            rs = self.queue2.pop(0)
            self.queue1.append(rs)
            return rs


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.queue1) + len(self.queue2)>0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()