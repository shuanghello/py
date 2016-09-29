#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
l=[x*x for x in range(1,101)]
print(l)
#如果直接用生成器 () 则l时不能直接打印出来的
#会抛出错误信息：<generator object <genexpr> at 0x10826aeb0>
g=(x*x for x in range(1,101))
#print(g)
#创建l和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
#我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值： 
print(g.next())
print(next(g))


