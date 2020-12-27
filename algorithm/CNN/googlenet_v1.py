#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/27
    @desc:
"""
import torch
import torch.nn as nn


class GooleNet(nn.Module):
    def __init__(self, num_class=4096):
        super(GooleNet, self).__init__()
        self.num_class = num_class
        self.create_model()
