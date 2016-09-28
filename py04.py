#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#递归
#写法一
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(100))
#这种写法党数值大的时候就会 异常(栈溢出)
#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中
#print(fact(3000))
#写法二
def fact02(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
         return product
    return fact_iter(num - 1,num * product)

print(fact02(100))

#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。