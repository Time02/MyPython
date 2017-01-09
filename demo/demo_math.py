#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

# 求解ax2 + bx + c = 0
def quadratic(a,b,c):
    num = [a,b,c]

    for i in num:
        if not isinstance(i,(int,float)):
            # raise TypeError('bad operand type')
            return '非数字'
    if a == 0:
        return '不可为0'
    else:
        d = b*b-4*a*c
        if d < 0 :
            return '不可对负数开方'
        else:
            x1 = (math.sqrt(d)-b)/(2*a)
            x2 = (-math.sqrt(d)-b)/(2*a)
            return x1,x2

print(quadratic(1.1,9,'44'))