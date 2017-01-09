#!/usr/bin/python
# -*- coding: utf-8 -*-

def recursion(n):
    return recursion_iter(n,1)

def recursion_iter(num,lastres):
    if num == 1:
        return lastres
    return recursion_iter(num - 1, num * lastres)

# print(recursion(101))

# 汉诺塔移动,它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
def move(n,a='A',b='B',c='C'):
    if n == 1:
        print('%s->%s'%(a,c))
        return None
    else:
        move(n-1,a,c,b)
        print('n是：%s，把%s->%s'%(n-1,a,c))
        move(n-1,b,a,c)
    return None

move(4)


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)