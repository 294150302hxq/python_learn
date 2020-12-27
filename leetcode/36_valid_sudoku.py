#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/12/21
    @desc:
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows_check = []
        for i in range(9):
            rows_check.append([])

        cols_check  = []
        for i in range(9):
            cols_check.append([])

        block_check = []
        for i in range(3):
            block_check.append([])
            for j in range(3):
                block_check[i].append([])

        for index,rows in enumerate(board):
            for i, ele in enumerate(rows):
                if ele != '.':
                    rows_check[index].append(ele)
                    cols_check[i].append(ele)
                    block_check[i//3][index//3].append(ele)
        for row in rows_check:
            if len(set(row)) < len(row): return False
        for col in cols_check:
            if len(set(col)) < len(col): return False
        for row_block in block_check:
            for block in row_block:
                if len(set(block)) < len(block): return False
        return True