#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2019/12/9
    @desc:
"""

print "Enter your name:", # 为了输入不换行，􏴝号􏰐以用􏰩􏱈多􏰑 print 语句合􏱝􏰌同一行􏱏􏰠
name = raw_input()

# 记得，需要空格以便更好看？print 用逗号分开会自己加上空格
print "hi", name, "how are you?"

# 使用raw_input直接提示
name = raw_input("Enter your name:")
print "hi", name, "how are you?"

# 从互联网中获得输入
import urllib2
file = urllib2.urlopen('http://helloworldbook2.com/data/message.txt')
message = file.read()
print message

# homework 1
first_name = raw_input("enter you first name:")
last_name = raw_input("enter you last name:")
print last_name,first_name


