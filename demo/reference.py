#!/usr/bin/python
# Filename: reference.py

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist
del mylist[0] #或者 del shoplist[0] 效果一样，因为指向同一个对象

print('shoplist is', shoplist)
print('mylist is', mylist)
# 这里 打印出来是一样的
#

print('Copy by making a full slice')
mylist = shoplist[:] # 通过一个完整的切片做一个拷贝
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 现在 他俩是不一样的