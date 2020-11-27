#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/27
    @desc:
"""

import torch
import torch.nn as nn


class VGGNet(nn.Module):
    def __init__(self, cfg, num_class=10, bn=False):
        super(VGGNet, self).__init__()
        self.num_class = num_class
        self.base = self.create_model(cfg, bn)
        self.fc1 = nn.Sequential(nn.Linear(512 * 8 * 8, 4096),
                                 nn.ReLU(inplace=True),
                                 nn.Dropout())
        self.fc2 = nn.Sequential(nn.Linear(4096, 4096),
                                 nn.ReLU(inplace=True),
                                 nn.Dropout())
        self.fc3 = nn.Linear(4096, num_class)

    def create_model(self, cfg, bn=False):
        layers = []
        in_channels = 3
        for layer_cfg in cfg:
            if layer_cfg == 'MaxPool':
                layers.append(nn.MaxPool2d((2, 2), stride=2))
            else:
                out_channels, kernel_size = layer_cfg.split("_")
                out_channels, kernel_size = int(out_channels), int(kernel_size)
                if bn:
                    layers.append(nn.Conv2d(in_channels, out_channels, (kernel_size,kernel_size), padding=1))
                    layers.append(nn.BatchNorm2d(out_channels))
                    layers.append(nn.ReLU(inplace=True))
                else:
                    layers.append(nn.Conv2d(in_channels, out_channels, (kernel_size, kernel_size), padding=1))
                    layers.append(nn.ReLU(inplace=True))
                in_channels = out_channels
        return nn.Sequential(*layers)

    def forward(self, x):
        batch_size = x.size()[0]
        x = self.base(x)
        print(x.size())
        x = x.view(batch_size, -1)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


if __name__ == '__main__':
    input_tensor = torch.randn((1, 3, 224, 224))
    input_var = torch.autograd.Variable(input_tensor)
    cfg = ['64_3', '64_3', 'MaxPool',
                '128_3', '128_3', 'MaxPool',
                '256_3', '256_3', '256_1', 'MaxPool',
                '512_3', '512_3', '512_1', 'MaxPool',
                '512_3', '512_3', '512_1', 'MaxPool']
    model = VGGNet(cfg, num_class=10)
    output = model(input_var)
    print(output.size())