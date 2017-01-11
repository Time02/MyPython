# -*- coding: utf-8 -*-

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
        print(i)
    return fs

f1, f2, f3 = count()
print(f1())
e = range(3)
print(e)
print([i for i in range(1,4)])