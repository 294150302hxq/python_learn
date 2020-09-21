#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/9/15
    @desc:
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.findPath(root, p)
        # print(p_path)
        q_path = self.findPath(root, q)
        # print(q_path)
        rs = None
        for index, node in enumerate(p_path):
            if len(q_path) > index and node == q_path[index]:
                rs = node
        return rs

    def findPath(self, root, node):
        path = []
        while node.val != root.val:
            path.append(root)
            if node.val > root.val:
                root = root.right
            else:
                root = root.left
        path.append(node)
        return path