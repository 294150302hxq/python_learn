#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2019/12/16
    @desc:
"""

# counting loop
for looper in range(5):
    print looper, "* 8 =", looper*8

# 字符串实际上是字符列表
for letter in 'hello!':
    print letter

# 倒计时
import time
for i in range(5,0,-1):
    print i
    time.sleep(1)
print "blast off!"

# conditional loop
print "Type 1 to continue, anything else to quit!"
num = int(raw_input())
while num == 1:
    print "you type", num
    print "Type 1 to continue, anything else to quit!"
    num = int(raw_input())

# homework
a = int(raw_input("Which multiplication table would you like?"))
b = int(raw_input("how high do you want to go?"))
print "Here's your table:"
for i in range(1, b+1):
    print a, "x", i, "=", a*i

# i = 1
# while i <= b:
#     print a, "x", i, "=", a * i
#     i += 1