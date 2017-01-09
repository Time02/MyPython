#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

res = [x * x for x in range(1,11)]

print(res)

res = [x * x for x in range(1,11) if x % 2 == 0]

print(res)

res = [m + n for m in 'ABC' for n in '123']

print(res)

res = [d for d in os.listdir('../')]

print(res)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k,'=>',v)

res = [k + '=' + v for k, v in d.items()]
print(res)