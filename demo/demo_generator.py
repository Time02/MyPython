#!/usr/bin/python
# -*- coding: utf-8 -*-

l = [x * x for x in range(10)]
print(l)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
print(g)

print(next(g))
print(next(g))

for i in g:
    print(i)

# 斐波那契数列
    def fibnc(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a + b
            n = n + 1
        return 'done !'

fibnc(10)