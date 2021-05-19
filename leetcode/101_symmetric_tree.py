#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-05-19
# @Author : duliri_hxq


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return True
        left_tree = [root.left]
        right_tree = [root.right]
        while left_tree != [] and right_tree != []:
            left_node = left_tree.pop(0)
            right_node = right_tree.pop(0)
            if left_node is None and right_node is None:
                pass
            elif left_node is not None and right_node is not None and left_node.val == right_node.val:
                left_tree += [left_node.left, left_node.right]
                right_tree += [right_node.right, right_node.left]
            else:
                return False
        return True