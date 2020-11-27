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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        node_queues = [[root]]
        final_rs = []
        while len(node_queues) > 0:
            node_queue = node_queues.pop(0)
            rs = []
            new_node_queue = []
            for node in node_queue:
                if node is not None:
                    rs.append(node.val)
                    new_node_queue.append(node.left)
                    new_node_queue.append(node.right)
            if rs:
                final_rs.append(rs)
            if new_node_queue:
                node_queues.append(new_node_queue)
        return final_rs


