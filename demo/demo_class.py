#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(self):
        print('%s: %s' % (self.name, self.score))

susan = Student('33','33')
susan.get_score()


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        print('s%: s%' % (self.__name, self.__score))


susan = Student('susan', 99)

print(susan._Student__name) # 用来理解，少用

# susan.__name # 会报错

print(isinstance(susan,Student))

print(type(susan))
print(type(1223))

#判断一个对象是否是函数
import types

def fn():
    pass

print(type(fn)==types.FunctionType)

print(dir('aa'))

class Screen():
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        print('resolustion : %s * %s = %s' % (self._width,self._height,self._height * self._height))

s = Screen()
s.width = 100
s.height = 200
s.resolution