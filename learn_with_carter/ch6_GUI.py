#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2019/12/9
    @desc:
"""
import easygui,random
# msgbox
# rs = easygui.msgbox("hello,my girl!")
# print rs

# button box
# fr = easygui.buttonbox("what's your favorite fruit?",choices=['apple', 'pear', 'orange'])
# easygui.msgbox("haha, I know your favorite fruit is "+fr)

# choice box
# fr = easygui.choicebox("what's your favorite fruit?",choices=['apple', 'pear', 'orange'])
# easygui.msgbox("haha, I know your favorite fruit is "+fr)

# enter box
# fr = easygui.enterbox("what's your favorite fruit?",default="grape")
# easygui.msgbox("haha, I know your favorite fruit is "+fr)

# guess number game
secret = random.randint(0,99)
print secret
for i in range(0,5):
    # rs = easygui.integerbox("please enter the number your guess?(0-99)")
    rs = int(easygui.enterbox("please enter the number your guess?(0-99)")) # 这种方式同上面一致，但是一定记着转化，不然对比有问题。
    if rs == secret:
        easygui.msgbox("you are so clever!")
        break;
    elif rs < secret:
        easygui.msgbox("It is too low!")
    else:
        easygui.msgbox("It is too high!")

if secret <> rs:
    easygui.msgbox("What a pity,please try again!")