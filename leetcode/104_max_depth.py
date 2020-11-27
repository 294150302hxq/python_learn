#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/22
    @desc:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        node_queue = [root]
        n = 0
        while node_queue:
            n += 1
            node_num = len(node_queue)
            for i in range(node_num):
                node = node_queue.pop(0)
                if node.left: node_queue.append(node.left)
                if node.right: node_queue.append(node.right)
        return n