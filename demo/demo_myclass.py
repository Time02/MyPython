#!/usr/bin/python
# -*- coding: utf-8 -*-

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __str__(self):
        return 'Fib object (a: %s)' % self.a

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    __repr__ = __str__

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


print(Fib())

f = Fib()
for n in Fib():
    print(n)


print(f[10])

# 应用
class Chain(object):

    def __init__(self, path='',name=''):
        self._path = path
        self.name = name

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __call__(self):
        print('My name is %s.' % self.name)

c = Chain('','name')
print(c.user.list.test)

c()