python解释器

要运行代码，就需要Python解释器去执行.py文件。
官方版本的解释器：CPython。这个解释器是用C语言开发的

IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的

CPython用>>>作为提示符，而IPython用In [序号]:作为提示符。

PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。

绝大部分Python代码都可以在PyPy下运行，但是PyPy和CPython有一些是不同的，这就导致相同的Python代码在两种解释器下执行可能会有不同的结果。如果你的代码要放到PyPy下执行，就需要了解PyPy和CPython的不同点。

Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。

IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。

Python的解释器很多，但使用最广泛的还是CPython。如果要和Java或.Net平台交互，最好的办法不是用Jython或IronPython，而是通过网络调用来交互，确保各程序之间的独立性。


直接运行py文件

像.exe文件那样直接运行.py文件，在Windows上是不行的，在Mac和Linux上是可以的，方法是在.py文件的第一行加上一个特殊的注释：

#!/usr/bin/env python3

print('hello, world')

然后，通过命令给hello.py以执行权限：

$ chmod a+x hello.py

就可以直接运行hello.py了，比如在Mac下运行：



输出和输出

print()会依次打印每个字符串，遇到逗号“,”会输出一个空格


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

- 数据类型

-- 整数：Python 可以处理任意大小的整数，
> Python的整数没有大小限制。Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
-- 浮点数：对于很大或者很小的数，必须使用科学计数法：1.23x109就是1.23e9 或者12.3e8，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
> 10/3 = 3.3333333333333335
还有一种除法是//，称为地板除，两个整数的除法仍然是整数：10//3 = 3
取余 %

-- 字符串：r''表示''内部的字符串默认不转义
-- 布尔值 True ，False
-- 空值：空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

-- 变量：可以处理不同类型的值，称为数据类型。基本的类型是数和字符串，和php 不同的是 Python 不允许类型隐式转换

-- 常量：习惯大写的变量名表示，

字符串和编码

ord()函数获取字符的整数表示
chr()函数把编码转换为对应的字符

由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

Python对bytes类型的数据用带b前缀的单引号或双引号表示：x = b'ABC'

1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。


格式化

%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%f表示浮点数替换，%x表示16进制整数，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

转义：用%%来表示一个%
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

是一个可变有序表，类比 php 中的索引数组,(可以多维),
len(shoplist) 数组长度
shoplist.append('rice')添加一个元素
print(shoplist)直接打印出来，
shoplist.sort() 排序，影响的是列表本身
del shoplist[0]，删除一个元素
shoplist.insert(1, 'Jack')，插入到指定位置
shoplist.pop(),删除末尾元素
shoplist.pop(i),删除指定元素




9.2 元组 tuple

元组合列表十分相似，但是元组不可变
可以是多维元组
空元组是一个括号，
单个元素元组，singleton = (2 , ) 这样Python才能区分元组和表达式中一个带圆括号的对象。
> 但是 元组中存进去 列表，列表位置不可变， 但是内部元素可变



print语句可以使用跟着 % 符号的项目元组的字符串。这些字符串具备定制的功能。定制让输出满足某种特定的格式。定制可以是%s表示字符串或%d表示整数。元组必须按照相同的顺序来对应这些定制。+

age = 22
name = 'Swaroop'

print '%s is %d years old' % (name, age)
print 'Why is %s playing with that python?' % name

9.3 字典

类比 php 中的 关联数组 (可以多维)
记住字典中的键/值对是没有顺序的。如果你想要一个特定的顺序，那么你应该在使用前自己对它们排序。

字典是dict类的实例/对象

d = {key1 : value1, key2 : value2 }
d[key3] = value3
del[key3]

字典的items方法，来使用字典中的每个键/值对。这会返回一个元组的列表，其中每个元组都包含一对项目——键与对应的值。

for name, address in ab.items():
    print('Contact %s at %s' % (name, address))

表示这个遍历很有意思啊，


9.4 序列

列表，元组和字符串都是序列，序列的两个主要特点是索引操作符和切片操作符。索引操作符让我们可以从序列中抓取一个特定项目。切片操作符让我们能够获取序列的一个切片，即一部分序列。

shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist[0]
shoplist[-1] #banana
name = 'time'
name[1:-1] #im
索引同样可以是负数，在那样的情况下，位置是从序列尾开始计算的。因此，shoplist[-1]表示序列的最后一个元素而shoplist[-2]抓取序列的倒数第二个项目。

切片操作符是序列名后跟一个方括号，方括号中有一对可选的数字，并用冒号分割。注意这与你使用的索引操作符十分相似。记住数是可选的，而冒号是必须的。

切片操作符中的第一个数（冒号之前）表示切片开始的位置，第二个数（冒号之后）表示切片到哪里结束。如果不指定第一个数，Python就从序列首开始。如果没有指定第二个数，则Python会停止在序列尾。注意，返回的序列从开始位置 开始 ，刚好在 结束 位置之前结束。即开始位置是包含在序列切片中的，而结束位置被排斥在切片外。


9.5 名称到对象的绑定

当你创建一个对象并给它赋一个变量的时候，这个变量仅仅 参考 那个对象，而不是表示这个对象本身！也就是说，变量名指向你计算机中存储那个对象的内存。这被称作名称到对象的绑定。

9.6 字符串也是对象

字符串也是对象，同样具有方法，符串都是str类的对象，参见help(str)

name = 'Swaroop' 
if name.startswith('Swa'):
if 'a' in name:
if name.find('war') != -1:

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist) #Brazil_*_Russia_*_India_*_China  作为分隔符的字符串join序列的项目的整洁的方法，它返回一个生成的大字符串。

10.1 写一个可以为我的所有重要文件创建备份的程序。

- 指定需要备份的文件和目录
- 存储到指定目录，
- 打包为一个时间命名的zip

zip命令有一些选项和参数。-q选项用来表示zip命令安静地工作。-r 对目录递归地工作。两个选项可以组合成缩写形式-qr。选项后面跟着待创建的zip归档的名称，然后再是待备份的文件和目录列表。我们使用已经学习过的字符串join方法把source列表转换为字符串。

os.system函数.在shell中运行命令——如果命令成功运行，它返回0，否则它返回错误号。

Windows 环境下 Windows把反斜杠（\）作为目录分隔符，而Python用反斜杠表示转义符！ 所以，你得使用转义符来表示反斜杠本身或者使用自然字符串。例如，使用'C:\\Documents'或r'C:\Documents'而不是'C:\Documents'——你在使用一个不知名的转义符\D！