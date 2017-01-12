# -*- coding: utf-8 -*-
import functools

def now():
    print('2017-1-12')

f = now
f()
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-1-12')

now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('test')
def now():
    print('2017-1-12')

now()

#-------在函数前后打印日志

def log(text = 'default'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('iter : %s ;begin call %s():' % (text, func.__name__))
            temp = func(*args, **kw)
            print('iter : %s ;end call %s():' % (text, func.__name__))
            return temp
        return wrapper
    return decorator

@log()
def now():
    print('now is :2017-1-12')

now()
