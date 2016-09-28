#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
def may_abs(x):
    if x>0:
        print('hehe')
    elif x>-2:
        print('heihei')
    else:
        print('hah')
    return(-x)
print(may_abs(1232))
#如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def may_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('参数类型不对')
    if x>0:
        print('hehe')
    elif x>-2:
        print('heihei')
    else:
        print('hah')
    return(-x)

#print(may_abs('21'))\

#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2))
#list 最为默认参数时
def add_end(l=[]):
    l.append('end')
    return l
#先传人默认值
print(add_end([1,2]))
#不传入默认值
print(add_end())
print(add_end())
print(add_end())
#结果发现 不传入值  累加调用也有值,原因如下：
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#定义默认参数要牢记一点：默认参数必须指向不变对象！
#我们可以用None这个不变对象来实现
def add_end_none(l=None):
    if l is None:
        l=[]
    l.append('end')
    return l
#与上面的调用 add_end() 输出结果对比
print(add_end_none())
print(add_end_none())
print(add_end_none())
print(add_end_none())
print(add_end_none())

#可变参数
#使用方法：在参数前面加了一个*号
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def cals(*nbers):
     sum=0
     print(nbers)
     for n in nbers:
        sum=sum+n
     return sum


print(cals(1,2,3))
#直接使用list 当可变参数使用
numlist = [ 2, 3, 4, 5, 6, 7, 8, 9 ]
print(cals(*numlist))

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('张三',15,city='beijing')
#命名关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
#命名关键字参数必须传入参数名，这和位置参数不同
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')
#person('Jack', 24, city='Beijing', job002='Engineer')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('Jack', 24, 'Beijing', 'Engineer', city='Beijing', job='Engineer')


