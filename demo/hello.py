#!/usr/bin/python
# Filename: hello.py
x = False
print(not x)

num1 = 99
num2 = 100
running = True

while running:
    if num1 == num2:
        print('相等')
    elif num1 < num2:
        print('小于')
        running = False
    else:
        print('大于')
else:
    print('The while loop is over.')

# for 语句
for i in range(1,4):
    print(i)
else:
    print('The for loop is over')


def func1(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

x = 50
func1(x)
print('x is still', x)


def func2():
    global x

    print('x is', x)
    x = 2
    print('Changed local x to', x)

x = 50
func2()
print('Value of x is', x)

global y
def func3(y):
    print('y is', y)
    y = 2
    print('Changed local y to', y)

y = 50
func3(y)
print('y is still', y)