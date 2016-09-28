#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list／tuple切片
#取前3个元素，用一行代码就可以完成切片
#从索引0开始取，直到索引3为止，但不包括索引3
L=['001','002','003','004','005']
print(L[0:3])
#0，可以省略
print(L[:3])
print(L[-2:])
#[:]就可以原样复制一个list
print(L[:])
m=list(range(100))
#每5个取一个
print(m[::5])
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#dict也可以进行迭代
d={'name':'li','sex':'man'}
for key in d:
    print(key+':'+d[key])
#dict迭代的是key。如果要迭代value，可以用for value in d.values()，
for hh in d.values():
    print(hh)
#如果要同时迭代key和value，可以用for k, v in d.items()
for ite in d.items():
    print(ite)

#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
#Iterable 翻译 可迭代
#instance 翻译 实例
from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3,4,5],Iterable))
print(isinstance(123,Iterable))

#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['a','s','d','f']):
    print(i,value)
#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)

#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#要生成[1x1, 2x2, 3x3, ..., 10x10]
listres = []
for i in list(range(1,11)):
    listres.append(i*i)
print(listres)
#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
print([x * x for x in range(1, 11)])
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x*x for x in range(1,11) if x%2==0])
#还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os #导入os模块
print([d for d in os.listdir('.')])