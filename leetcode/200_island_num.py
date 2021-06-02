#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 2021-06-02
# @Author : duliri_hxq
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        rs = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    rs += 1
                    index_list = [(i, j)]
                    while len(index_list) > 0:
                        x, y = index_list.pop()
                        grid[x][y] = '0'
                        for row, col in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= row < m and 0 <= col < n and grid[row][col] == '1':
                                index_list.append((row, col))
        return rs
