#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/10/9
    @desc:
"""

import torch
import torch.nn as nn

class AlexNet(nn.Module):
    def __init__(self, num_class=4096):
        super(AlexNet, self).__init__()
        self.num_class = num_class
        self.create_model()

    def create_model(self):
        # maxpool(relu(x)) = relu(maxpool(x)), to reduce time we can use relu(maxpool(x))
        # but it doesn't work in all situations, like avgpool
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 96, (11, 11), stride=4, padding=2),
            nn.MaxPool2d((3, 3), stride=2),
            nn.ReLU(inplace=True))

        self.conv2 = nn.Sequential(
            nn.Conv2d(96, 256, (5, 5), stride=1, padding=2),
            nn.MaxPool2d((3, 3), stride=2),
            nn.ReLU(inplace=True))

        self.conv3 = nn.Sequential(
            nn.Conv2d(256, 384, (3, 3), stride=1, padding=1),
            nn.ReLU(inplace=True))

        self.conv4 = nn.Sequential(
            nn.Conv2d(384, 384, (3, 3), stride=1, padding=1),
            nn.ReLU(inplace=True))

        self.conv5 = nn.Sequential(
            nn.Conv2d(384, 256, (3, 3), stride=1, padding=1),
            nn.MaxPool2d((3, 3), stride=2),
            nn.ReLU(inplace=True))

        self.classifier = nn.Sequential(
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(4096, self.num_class)
        )

    def forward(self, x):
        x = self.conv1(x)
        print(x.size())
        x = self.conv2(x)
        print(x.size())
        x = self.conv3(x)
        print(x.size())
        x = self.conv4(x)
        print(x.size())
        x = self.conv5(x)
        print(x.size())
        x = x.view(x.size(0), -1)
        print(x.size())
        x = self.classifier(x)
        print(x.size())
        return x


if __name__ == '__main__':
    input_tensor = torch.randn((1, 3, 224, 224))
    input_var = torch.autograd.Variable(input_tensor)
    model = AlexNet(num_class=1000)
    print(model)
    output = model(input_var)