
在Python中有4种类型的数——整数、长整数、浮点数和复数。+

2是一个整数的例子。
长整数不过是大一些的整数。
3.23和52.3E-4是浮点数的例子。E标记表示10的幂。在这里，52.3E-4表示52.3 * 10<sup>-4</sup>。
(-5+4j)和(2.3-4.6j)是复数的例子。

字符串
单引号 ，双引号 ， 三引号：指示多行字符串，内部自由使用单双引号，

- 转义符， \' = \  \\ = \
双引号 内可以识别 单引号

在一个字符串中， 行末的单独一个反斜杠 \ 表示字符串在下一行继续，

- 自然字符串

不需要入转义符那样子的特殊处理。那就要制定一个自然字符串，

- unicode
Python允许你处理Unicode文本——你只需要在字符串前加上前缀u或U。例如，u"This is a Unicode string."。

- 字符串是不可变的
这意味着一旦你创造了一个字符串，你就不能再改变它了。虽然这看起来像是一件坏事，但实际上它不是。我们将会在后面的程序中看到为什么我们说它不是一个缺点。

- 按字面意义级连字符串
如果你把两个字符串按字面意义相邻放着，他们会被Python自动级连。例如，'What\'s' 'your name?'会被自动转为"What's your name?"。


给Perl/PHP程序员的注释，记住，单引号和双引号字符串是完全相同的——它们没有在任何方面有不同。
给正则表达式用户的注释 一定要用自然字符串处理正则表达式。否则会需要使用很多的反斜杠。例如，后向引用符可以写成'\\1'或r'\1'。



变量

我们需要一种既可以储存信息 又可以对它们进行操作的方法，变量只是你的计算机中存储信息的一部分内存


标识符

标识符 是用来标识 某样东西 的名字
第一个字符由大小写字母和下划线，其他字符由大小写字母和下划线和数字

数据类型

变量可以处理不同类型的值，称为数据类型。基本的类型是数和字符串，和php 不同的是 Python 不允许类型隐式转换

物理行与逻辑行

物理行是你在编写程序时所 看见 的。逻辑行是Python 看见 的单个语句。

默认地，Python希望在每个物理行只写一句逻辑行，这样使得代码更加易读。

如果你想要在一个物理行中使用多于一个逻辑行，那么你需要使用分号（;）来特别地标明这种用法。分号表示一个逻辑行/语句的结束。

\可以做为换行链接

print \
i

和 print i  一样

时候，有一种暗示的假设，可以使你不需要使用反斜杠。这种情况出现在逻辑行中使用了圆括号、方括号或波形括号的时候。这被称为暗示的行连接。

第5章 运算符与表达式

运算符， 和 php 很不一样啊 ：）

+ 两个对象相加，3+5=8  'a'+'b' ='ab'; 

- 正常数学运算， 字符串的减会报错哈哈，TypeError: unsupported operand type(s) for -: 'str' and 'str'

* 两个数相乘或是返回一个被重复若干次的字符串，2 3得到6。'la' 3得到'lalala'。

** 幂 返回x的y 次幂，

/ 除法

// 取整除，4 // 3.0得到1.0

% 取模，返回除法的余数

<< 左移，把一个数的比特向左移一定数目（每个数在内存中都表示为比特或二进制数字，即0和1）
2 << 2得到8。——2按比特表示为10

& 数的按位与 5 & 3得到1。

| 数的按位或 5 | 3得到7。

^ 数的按位异或，5 ^ 3得到6

~ 数的按位翻转 x的按位翻转是-(x+1)

< 返回是否小于 5 < 3返回0（即False）而3 < 5返回1（即True）。比较可以被任意连接：3 < 5 < 7返回True。

> 返回x是否大于y

<= 返回是否小于等于

>= 返回是否大于等于

== 比较对象是否相等

!= 比较对象是否不相等

not 布尔“非”，x = True; not y返回False。（注意，py 的False 和 True 首字母大写，和php 不一样）

and 布尔“与”

or 布尔“或”

与和 或 注意和php 一样的 短路计算

运算符优先级--

圆括号来分组运算符和操作数，可读性强，同时可以改变优先级
运算符通常由左向右结合，即具有相同优先级的运算符按照从左向右的顺序计算。
一些如赋值运算符那样的运算符是由右向左结合的，即a = b = c被处理为a = (b = c)。

表达式

length = 5
breadth = 2
area = length * breadth
print 'Area is', area

输出 Area is 10

> 尽管我们没有在'Area is'和变量area之间指定空格，Python自动在那里放了一个空格


控制流

Python 中有三种 控制流语句 if、for和while。

if语句

num1 = 100
num2 = 99

if num1 == num2:
    print('相等')
elif num1 < num2:
    print('小于')
else:
    print('大于')

# 把else-if 合并些为 elif

> python 中没有 switch 语句

while语句

while True:
    print('loop')
else:
    print('The while loop is over.')


for 语句

for i in 10:
    print i
else:
    print 'The for loop is over'


break 语句

停止，没什么区别

continue 语句

跳过当前循环块中的剩余语句，然后 继续 进行下一轮循环，也没什么区别

 
函数

函数通过def关键字定义。def关键字后跟一个函数的 标识符 名称，然后跟一对圆括号。圆括号之中放形参，该行以冒号结尾。接下来是一块语句，它们是函数体。

def sayHello():
    print 'Hello World!'

sayHello()


局部变量

当你在函数定义内声明变量的时候，它们与函数外具有相同名称的其他变量没有任何关系，即变量名称对于函数来说是 局部 的。这称为变量的 作用域 。所有变量的作用域是它们被定义的块，从它们的名称被定义的那点开始。


全局变量

如果你想要为一个定义在函数外的变量赋值，那么你就得告诉Python这个变量名不是局部的，而是 全局 的。我们使用global语句完成这一功能。

默认参数值

重要 只有在形参表末尾的那些参数可以有默认参数值，即你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。 这是因为赋给形参的值是根据位置而赋值的。例如，def func(a, b=5)是有效的，但是def func(a=5, b)是 无效 的。

 关键参数

 如果你的某个函数有许多参数，而你只想指定其中的一部分，那么你可以通过命名来为这些参数赋值——这被称作 关键参数 ——我们使用名字（关键字）而不是位置（我们前面所一直使用的方法）来给函数指定实参。

 不必担心参数顺序，

 def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)
输出
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50

return 语句

没有返回值的return语句等价于return None。None是Python中表示没有任何东西的特殊类型。例如，如果一个变量的值为None，可以表示它没有值。
除非你提供你自己的return语句，每个函数都在结尾暗含有return None语句。

pass语句在Python中表示一个空的语句块。

DocStrings

Python有一个很奇妙的特性，称为 文档字符串 ，它通常被简称为 docstrings 。

在函数的第一个逻辑行的字符串是这个函数的 文档字符串 。注意，DocStrings也适用于模块和类

你可以使用__doc__（注意双下划线）调用printMax函数的文档字符串属性（属于函数的名称）。请记住Python把 每一样东西 都作为对象，包括这个函数。


8章 模块

模块基本上就是一个包含了所有你定义的函数和变量的文件。为了在其他程序中重用模块，模块的文件名必须以.py为扩展名。

#!/usr/bin/python
# Filename: using_sys.py

import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'


我们利用import语句 输入 sys模块。sys模块包含了与Python解释器和它的环境有关的函数。
当Python执行import sys语句的时候，它在sys.path变量中所列目录中寻找sys.py模块。如果找到了这个文件，这个模块的主块中的语句将被运行，然后这个模块将能够被你 使用 。注意，初始化过程仅在我们 第一次 输入模块的时候进行。

sys.argv变量是一个字符串的 列表

这里，当我们执行python using_sys.py we are arguments的时候，我们使用python命令运行using_sys.py模块，后面跟着的内容被作为参数传递给程序。Python为我们把它存储在sys.argv变量中。

记住，脚本的名称总是sys.argv列表的第一个参数。所以，在这里，'using_sys.py'是sys.argv[0]、'we'是sys.argv[1]、'are'是sys.argv[2]以及'arguments'是sys.argv[3]


字节编译的.pyc文件

使输入模块更加快一些

8.1 from..import语句

如果你想要直接输入argv变量到你的程序中（避免在每次使用它时打sys.），那么你可以使用from sys import argv语句。如果你想要输入所有sys模块使用的名字，那么你可以使用from sys import *语句。这对于所有模块都适用。一般说来，应该避免使用from..import而使用import语句，因为这样可以使你的程序更加易读，也可以避免名称的冲突。

8.2模块的name
当一个模块被第一次输入的时候，这个模块的主块将被运行。假如我们只想在程序本身被使用的时候运行主块，而在它被别的模块输入的时候不运行主块，可以通过模块的name属性完成。

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'


每个Python模块都有它的__name__，如果它是'__main__'，这说明这个模块被用户单独运行，我们可以进行相应的恰当操作。


8.3制造你自己的模块

#!/usr/bin/python
# Filename: mymodule.py

def sayhi():
    print 'Hi, this is mymodule speaking.'

version = '0.1'

# End of mymodule.py

记住这个模块应该被放置在我们输入它的程序的同一个目录中，或者在sys.path所列目录之一。

使用这个自定义模块

#!/usr/bin/python
# Filename: mymodule_demo.py

import mymodule

mymodule.sayhi()
print 'Version', mymodule.version

下面是一个使用from..import语法的版本。

#!/usr/bin/python
# Filename: mymodule_demo2.py

from mymodule import sayhi, version
# 或者:
# from mymodule import *

sayhi()
print 'Version', version


8.5 dir() 函数

内置的dir函数来列出模块定义的标识符。标识符有函数、类和变量。

9 数据结构

在Python中有三种内建的数据结构——列表、元组和字典

9.1 列表
