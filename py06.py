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
#我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
for x in g:
    print(x)
#再次强调了：generator保存的是算法，而不是对应的值

#练习
#斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'Over'
print(fib(6))
#注意 下面两种情况的写法
#a=b b=a+b 正常的赋值
#a,b=b,a+b 这种写法 a+b 取得是a未赋值b的 时候的值
#延伸 a，b 交换数值
def changedounum(a,b):
    a,b=b,a
    print('a=%d  b=%d' %(a,b))
changedounum(1,2)

#yield语句返回，再次执行时从上次返回的yield语句处继续执行 
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o=odd()
print(next(o)) 
print(next(o)) 
print(next(o)) 



