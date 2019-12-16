#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2019/12/12
    @desc:
"""
# 代码块：python通过缩进来指出代码块开始和结束
age = int(raw_input("how old are you?"))
if 8 < age < 12: # 介于两者之间
    print "hi, my little girl!"
# 多条件判断：and、or、not（logical operator）
amount = float(raw_input("how much ?"))
if amount <= 10:
    print "it costs", amount*0.9
elif amount > 10:
    print "it costs", amount * 0.8
else:
    print "wrong number!"

# homework 1
gender = raw_input("what's your gender?")
if gender == 'f':
    age = int(raw_input("how old are you?"))
    if 10 <= age <= 12:
        print "you are in"
    else:
        print "sorry!"
else:
    print "sorry!"