#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/1/17
    @desc:
"""

import cPickle
import numpy as np

from learn_py_pak.DNN import Network


def load_data():
    with open('../data/mnist.pkl') as fp:
        training_data, valid_data, test_data = cPickle.load(fp)
    return training_data, valid_data, test_data  # training_data, valid_data, test_data 均是二元 tuple


def vectors(y):
    """赋予标签"""
    label = np.zeros((10, 1))
    label[y] = 1.0  # 浮点计算
    return label


if __name__ == '__main__':
    training_data, valid_data, test_data = load_data()
    print "the {0} size: {1}".format("training_data", len(training_data[0]))
    print "the {0} size: {1}".format("valid_data", len(valid_data[0]))
    print "the {0} size: {1}".format("test_data", len(test_data[0]))
    print "the {0} size: {1}".format("image", len(training_data[0][0]))
    print training_data[0]
    n = [np.reshape(x, (784, 1)) for x in training_data[0]]
    # 标签one-hot
    m = [vectors(y) for y in training_data[1]]
    tr_data = zip(n, m)  # 元组中有两个向量
    n = [np.reshape(x, (784, 1)) for x in valid_data[0]]  # 将5万个数据分别逐个取出化成（784,1），排列
    val_data = zip(n, valid_data[1])  # 没有将标签数据矢量化
    n = [np.reshape(x, (784, 1)) for x in test_data[0]]  # 将5万个数据分别逐个取出化成（784,1），排列
    te_data = zip(n, test_data[1])  # 没有将标签数据矢量化
    net1 = Network([784, 30, 10])
    min_batch_size = 10
    eta = 3.0
    epoches = 30
    net1.SGD(tr_data, min_batch_size, epoches, eta, te_data)
    print "complete"
