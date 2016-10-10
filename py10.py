#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python内建的filter()函数用于过滤序列。
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n % 2 == 1

print(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


'''
排序算法
sorted  
Python内置的sorted()函数就可以对list进行排序
'''
ls=[1,-2,3,2,9,11,4]
print(sorted([1,-2,3,2,9,11,4]))
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list
print(sorted(ls,key=abs))

#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
#现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
#这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
