#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#map/reduce
'''
Python内建了map()和reduce()函数。
如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。
我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
'''
def f(x):
    return x*x
r=map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
from collections import Iterator
print(isinstance(r,Iterator))
print(r)
#结果证明 并把结果作为新的Iterator返回  似乎是错误的
#返回的结果还是 Iterable  ⭐️

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
from functools import reduce
def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn,map(char2num, '13579')))