#!/usr/bin/python
# -*- coding: utf-8 -*-

'枚举'

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#value属性则是自动赋给成员的int常量，默认从1开始计数。

@unique # 保没有重复值的成员
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7

c = Color
print(Color['red']) #Color.red
print(Color['red'].name) # red
print(Color['red'].value) # 1

# 每一个成员都有它们各自名称和值，Color.red成员的名称是：red，值是：1。

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

print(type(Hello)) # <class 'type'>