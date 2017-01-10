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
print('斐波那契数列')

def fibnc(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done !'

for i in fibnc(10):
    print(i)

# 杨辉三角
print('杨辉三角')

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 2:
        break

l = [1]
l.append(0)
print(l)
l = [l[i - 1] + l[i] for i in range(len(l))]
print(l)