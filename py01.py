#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('李爽')
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('%2d' %123456789)
print('%d' %123456789)
print('%f' %123.2222222)
print('%0.2f' %123.2222222)
print('%d-%d' %(1,2))
#练习
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1=72
s2=85
r=s2/s1
print('%0.1f' %r)
#python list 长度用len
#索引可以为负数（表示从后向前的索引）
classname=['class01','class02','class03']
print('classname长度:%s' %len(classname))
print('classname第一个元素:%s' %classname[0])
print('classname第一个元素:%s' %classname[-3])
print('classname第二个元素:%s' %classname[1])
print('classname第二个元素:%s' %classname[-2])
print('classname第三个元素:%s' %classname[2])
print('classname第三个元素:%s' %classname[-1])
#list 添加元素使用append
classname.append('class04')
print('classname list length %d' %len(classname))
#list 把元素插入指定位置 insert  第一个参数表示插入的位置的索引
classname.insert(0,'class001')
print('classname第一个元素 %s' %classname[0])
#list 删除末尾元素 pop
print('删除前末尾元素为：%s' %classname[len(classname)-1])
classname.pop()
print('删除后末尾元素为：%s' %classname[len(classname)-1])

#list 删除指定的元素 pop(i) i为数组的索引
print('删除前索引为0的元素： %s' %classname[0])
classname.pop(0)
print('删除后索引为0的元素： %s' %classname[0])

#list 里面元素的数据类型可以不一样
#list 里面可以套用list

#tuple 与list 非常类似 但是tuple一担初始化就不能修改
#内容不能变更加安全
classmates = ('tuple01', 'typle02', 'tuple03')

#条件判断
#if <条件判断1>:
#    <执行1>
#elif <条件判断2>:
#    <执行2>
#elif <条件判断3>:
#    <执行3>
#else:
#    <执行4>
age=int(input())
if age>=18:
   print('老了')
elif age>=16:
   print('年轻')
else:
   print('小了')

#循环  循环代码块必须有缩进
# for .. in .. :
for itx in classname:
    print(itx)
#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
for itx in range(10):
    print(itx)
# while .. :
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#dict
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
dictname={'zs':12,'ls':13}
print(dictname['zs'])
#dict 插入
dictname['ls01'] = 90
print(dictname['ls01'])
#要避免key不存在的错误，有两种办法
#一是通过in判断key是否存在：
print('sss' in dictname)
#二dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(dictname.get('Thomas'))
print(dictname.get('Thomas', -1))
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
dictname.pop('ls01')
print(dictname)
######
#dict和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。

#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
print(s)
#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的
#重复元素在set中自动被过滤
s = set([1,1,2,2,4,3])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(8)
s.add(5)
s.add(5)
print(s)
#通过remove(key)方法可以删除元素
s.remove(4)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s12 = s1 & s2
s1122 = s1 | s2
print('交集：%s' %s12)
print('并集：%s' %s1122)
