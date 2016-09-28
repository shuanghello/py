#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#调用函数
#Python内置了很多有用的函数，我们可以直接调用。
#要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
#http://docs.python.org/3/library/functions.html#abs
#也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
print(abs)
#1.求绝对值 abs()
print(abs(-100))
#2.求最大值 max()
print(max(1,2,3,-1,6,1.99))
#3.转化为整数 int()
print(int('100'))
print(int(100.1))#print(int('100.1'))写成这样就是错误的  不能直接把浮点字符串转化为int   需要先把浮点字符串转化为浮点数 在转化
print(int(100.6))
#4.转化为浮点数 float()
print(float('100.332'))
#5.转化为字符串 str()
print(str(1000))
#6.转化为bool bool()
#转化bool规则 
#字符串  非空都为true
#数字  非0都为true
print(bool(1))
print(bool(0))
print(bool(-2))
print(bool(3))
print(bool('123'))
print(bool(''))
#更多内置函数 ：http://docs.python.org/3/library/functions.html#abs


