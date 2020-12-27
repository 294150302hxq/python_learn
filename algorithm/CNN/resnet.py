#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/11/28
    @desc:
"""

import torch
import torch.nn as nn


class BasicBlock(nn.Module):
    expansion = 1
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.block = nn.Sequential(self.conv1, self.bn1, self.relu, self.conv2, self.bn2)
        self.downsample = downsample
        # self.stride = stride

    def forward(self, x):
        residual = x
        out = self.block(x)
        if self.downsample:
            residual = self.downsample(x)
        out += residual
        out = self.relu(out)
        return out


class Bottleneck(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(Bottleneck, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1)
        self.bn1 = nn.BatchNorm2d(out_channels)

        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)

        self.conv3 = nn.Conv2d(out_channels, out_channels*4, kernel_size=1, stride=1)
        self.bn3 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)

        self.block = nn.Sequential(self.conv1, self.bn1, self.relu, self.conv2, self.bn2, self.relu, self.conv3, self.bn3)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        residual = x
        out = self.block(x)
        if self.downsample:
            residual = self.downsample(x)
        out += residual
        out = self.relu(out)
        return out



class ResNet(nn.Module):
    def __init__(self, block, layers, num_classes=1000):
        super(ResNet, self).__init__()
        self.pre = nn.Sequential(nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3), nn.BatchNorm2d(64),
                                 nn.MaxPool2d(kernel_size=3, stride=2), nn.ReLU(inplace=True))
        self.in_channels = 64
        self.layer1 = self._make_layer(block, layers[0])
        self.layer2 = self._make_layer(block, layers[1], stride=2)
        self.layer3 = self._make_layer(block, layers[2], stride=2)
        self.layer4 = self._make_layer(block, layers[3], stride=2)
        self.avgpool = nn.AvgPool2d(7, stride=1)
        self.fc = nn.Linear(512 * block.expansion, num_classes)

    def _make_layer(self, block, block_num, stride=1):
        # downsample 主要用来处理H(x)=F(x)+x中F(x)和x channel维度不匹配问题
        downsample = None
        # 一种是feature map的size是不同，一种是channel的不同
        out_channels = self.in_channels * block.expansion
        if stride != 1 or self.in_channels != out_channels:
            downsample = nn.Sequential(
                nn.Conv2d(self.in_channels, out_channels,
                          kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels),
            )
        layers = []
        layers.append(block(self.in_channels, out_channels, stride, downsample))
        self.in_channels = out_channels
        for i in range(1, block_num):
            layers.append(block(self.in_channels, out_channels))
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.pre(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x



def resnet18(**kwargs):
    """Constructs a ResNet-18 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [2, 2, 2, 2], **kwargs)
    return model


if __name__ == '__main__':
    # 1是batch size，3是channel，224*224是image size
    input_tensor = torch.randn((1, 3, 224, 224))
    input_var = torch.autograd.Variable(input_tensor)
    model = resnet18()
    print(input_var.size())
    output = model(input_var)
    print(output.size())
