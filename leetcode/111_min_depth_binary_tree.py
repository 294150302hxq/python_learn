#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/23
    @desc:
"""


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        all_depth = []
        self._dfs(1, root, all_depth)
        return min(all_depth)

    def _dfs(self, level, node, all_depth):
        if not node.left and not node.right:
            all_depth.append(level)
            return
        if node.left:
            self._dfs(level + 1, node.left, all_depth)
        if node.right:
            self._dfs(level + 1, node.right, all_depth)