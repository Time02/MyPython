#Python 笔记
一个 php coder 学习 Python 的笔记。环境 macOS，Python 3.6

##python解释器

###CPython

要运行代码，就需要Python解释器去执行.py文件。
官方版本的解释器：CPython。这个解释器是用C语言开发的

###IPython

IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的

CPython用>>>作为提示符，而IPython用In [序号]:作为提示符。

###PyPy

PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。

绝大部分Python代码都可以在PyPy下运行，但是PyPy和CPython有一些是不同的，这就导致相同的Python代码在两种解释器下执行可能会有不同的结果。如果你的代码要放到PyPy下执行，就需要了解PyPy和CPython的不同点。

###Jython

Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。

###IronPython

IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。

> Python的解释器很多，但使用最广泛的还是CPython。如果要和Java或.Net平台交互，最好的办法不是用Jython或IronPython，而是通过网络调用来交互，确保各程序之间的独立性。


##直接运行py文件

像.exe文件那样直接运行.py文件，在Windows上是不行的，在Mac和Linux上是可以的，方法是在.py文件的第一行加上一个特殊的注释：

```python
#!/usr/bin/env python3

print('hello, world')
```

然后，通过命令给hello.py以执行权限：

```shell
$ chmod a+x hello.py
```

就可以直接运行hello.py了，比如在Mac下运行：

```shell
./hello.py
```
##输出和输出

print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
input(),可以让用户输入字符串，返回的数据类型是str
> 输入是 Input，输出是 Output，因此，我们把输入输出统称为 Input/Output，或者简写为IO。 

## Python 基本概念

###数据类型和变量

####整数

在 Python 中有 4 种类型的数——整数、长整数、浮点数和复数。

- 整数
  Python 可以处理任意大小的整数。长整数不过是大一些的整数。但是超出一定范围就直接表示为inf（无限大）
- 浮点数
  3.23和52.3E-4是浮点数的例子。E标记表示10的幂。在这里，52.3E-4表示52.3 * 10<sup>4</sup>。
- 复数
  (-5+4j)和(2.3-4.6j)是复数的例子。

> 整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。10/3 = 3.3333333333333335
> 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：10//3 = 3
> 取余 %

####字符串

单引号，双引号，三引号：指示多行字符串，内部自由使用单双引号，

- 转义， \' = \  \\ = \
  双引号 内可以识别 单引号

在一个字符串中， 行末的单独一个反斜杠 \ 表示字符串在下一行继续
用'''...'''的格式表示多行内容

- 大字符串

不需要入转义符那样子的特殊处理。那就要制定一个自然字符串，
用r''表示''内部的字符串默认不转义


> 和 php 不一样，单引号和双引号字符串是完全相同的——它们没有在任何方面有不同。

####布尔值

True False ，可以进行布尔运算
> php 中大小写都可以

####空值

空值：空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的


####变量

可以处理不同类型的值，称为数据类型。基本的类型是数和字符串，和 php 不同的是 Python 不允许类型隐式转换

####常量

习惯大写的变量名表示，

###字符串和编码

8个比特（bit）作为一个字节（byte），一个字节最大表示255
> 最开始，只有 ASCII 编码（一个字节）。然后，中国制定了GB2312编码，用来把中文编进去。后来，Unicode（2个字节）把所有语言都统一到一套编码里，不会再有乱码问题了。最后，为了节省存储空间，出现了把 Unicode 编码转化为“可变长编码”的 UTF-8 编码。

Python的字符串支持多语言

ord()函数获取字符的整数表示
chr()函数把编码转换为对应的字符
encode()方法可以编码为指定的bytes
len()方法计算长度

####格式化

% 运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%f表示浮点数替换，%x表示16进制整数，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

> 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

> 转义：用%%来表示一个%

###列表和元组（list and tuple）

####list

有序可变集合，其中的元素可以是任何类型，类比 PHP 中的索引数组
索引：正序从 0 开始，倒序从 -1 开始

```python
shop = ['apple','bnaner','orange']
shop.append('tangerines') #列表末尾追加

shop.insert(1,'melons') #指定位置添加

shop.pop() # 删除末尾元素

shop.pop(1) # 删除指定位置的元素

shop.sort() # 排序

shop[1] = 'xxx' # 替换
```
> 可以有 [][] 这种写法

####tuple

tuple 和 list 类似，但是 tuple 一旦初始化不可修改。当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。

> 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

> 空的tuple，可以写成 shop = ()

> 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：shop = (1,)

> 其实元组里放入可变的 list ，在第二维就变成可变的了

###流程控制

####if else 的不同

elseif 可以缩写为 elif

####循环的不同

```python
shop = ['apple','bnaner','orange']

for v in shop:
    print(v) 
```
range(): 生成一个整数序列

###字典和集合（dict and set）

####字典

key-value，类比 PHP 中的关联数组。

key 不存在会报错，判断 key 是否存在：
- in 判断，返回 True False
- get 方法，返回 None 或存在的 value

删除：pop(key)
> dict内部存放的顺序和key放入的顺序是没有关系的。

和 list 比较：dict 查找插入极快，占用内存大

####集合

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：

```python
s = set([1, 2, 3])
print(s) #{1, 2, 3}
```
> 重复元素在set中自动被过滤：

- add(key) 添加元素，可以重复添加但是不会有效果
- remove(key)删除元素

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

```python
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2 # {2, 3}
s1 | s2 # {1, 2, 3, 4}
```

##函数

###调用函数

[doc][1]

- abs() 求绝对值

> 如果函数的参数不正确，会报 TypeError 错误

- max() 参数为任意多个，返回最大的
- int() 转换为整形
- float() 转浮点型
- str() 转字符型
- bool() 转布尔型

函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
```python
a = abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数
```

###定义函数

使用 def 语句，一次：函数名，括号，参数，冒号，代码块，return 返回

> 函数执行完毕后也会返回结果，只是结果为None。

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

如果你已经把 my_abs() 的函数定义保存为 abstest.py 文件了，那么，可以在该文件的当前目录下启动 Python 解释器，用 from abstest import my_abs 来导入 my_abs() 函数，注意 abstest 是文件名（不含.py扩展名）：

####空函数

定义一个什么也不做的函数

```python
def nop():
    pass
```

> 这里 pass 起了一个占位符作用，去掉会报错

####参数检查

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError

但是如果参数类型不对，Python解释器就无法帮我们检查。

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

```

> 和 isinstance  作用类似的还有 type函数
>
> type('foo') == str ,type(2.3) in (int,float)，
>
> 两者区别是：type()不会认为子类是一种父类类型。
> isinstance()会认为子类是一种父类类型。

####返回多个值

```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x = move(100, 100, 60, math.pi / 6) 
print(x) # 这里返回一个元组
    
```

> 这里和 PHP 返回多个值一样，放数组里


###函数的参数

- 必须按参数在前，默认参数在后
- 注意默认参数也是一个变量,所以默认参数必须指向不变的对象：

```python
def add_end(L=[]):
    L.append('END')
    return L

add_end([1, 2, 3]) # [1, 2, 3, 'END']

add_end() # ['END']
add_end() # ['END','END']

# 使用 None 修改

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

####可变参数

*numbers 代表接受到的是一个元组 tuple，此时可以传入任意哥参数。

```python
# 给定一组数字 a，b，c……，请计算 a2 + b2 + c2 + ……。

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
  
res = calc(1,2,3)
```

如果方法要调用 list 中的每一个值

```python
nums = [1, 2, 3]
calc(*nums) # 14
```

####关键字参数

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer')
#输出：name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# 输出：name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

# 这里传进去的字典是一份 copy

```

####命名关键字参数

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

仍以 person()函数为例，我们希望检查是否有 city 和 job 参数：

```python
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
    
#但是调用者仍可以传入不受限制的关键字参数
```

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收 city 和 job 作为关键字参数。这种方式定义的函数如下：

```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

和关键字参数 **kw 不同，命名关键字参数需要一个特殊分隔符 * ，* 后面的参数被视为命名关键字参数。

> 一个 * 是 tuple （列表->PHP 索引数组），** 是 dict （字典->PHP 关联数组）

```python
res = person('Jack', 24, city='Beijing', job='Engineer')
print(res) # Jack 24 Beijing Engineer
```

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```

命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：

```python
person('Jack', 24, 'Beijing', 'Engineer')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given
```


####参数组合

在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。







#### 递归函数

在函数内部调用自身。比如计算阶乘

```python
    def recursion(n)
        if n == 1:
            return 1
        return n * recursion(n-1)
    #函数运行过程，以 recursion(5) 为例：
    # recursion(5)
    # 5 * recursion(4)
    # 5 * (4 * recursion(3))
    # 5 * (4 * (3 * recursion(2)))
    # 5 * (4 * (3 * (2 * recursion(1))))
```

使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试：recursion(1000) 会报错。

解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

```python
    def recursion(n):
        return recursion_iter(n,1)
    def recursion_iter(n,lastres):
        if n == 1:
            return lastres
        return recursion_iter(n-1, n*lastres)
    # 例子：recursion(5):
    # recursion_iter(5, 1)
    # recursion_iter(4, 5)
    # recursion_iter(3, 20)
    # recursion_iter(2, 60)
    # recursion_iter(1, 120)
```

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

一个 demo [汉诺塔][2] :  ps: 目前还未彻底搞明白 : (

```python
def move(n,a='A',b='B',c='C'):
    if n == 1:
        print('%s->%s'%(a,c))
        return None
    else:
        move(n-1,a,c,b)
        print('n是：%s，把%s->%s'%(n-1,a,c))
        move(n-1,b,a,c)
    return None
```

## 高级特性

在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

### 切片

list 或 tuple 或字符串都可以进行切片操作

```python
shop = ['apple','bnaner','orange','melons','pear']
#取前三个元素, 顺序是0开始， 倒序是 -1
shop[0:3]

#前4个数，每两个取一个：
shop[0:3:2]

#所有数，每2个取一个：
shop[::2]
```

### 迭代

我们把循环遍历称为迭代。



断一个对象是可迭代对象：collections模块的Iterable类型判断

```python
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代 True
isinstance([1,2,3], Iterable) # list是否可迭代 True
isinstance(123, Iterable) # 整数是否可迭代 False
```



### 列表生成式

列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

例如生成 [1x1, 2x2, 3x3, ..., 10x10] 怎么做？方法一是循环，而列表生成更简洁：

```python
res = [x * x for x in range(1,11)]
print(res)

# 筛选出仅偶数的平方
res = [x * x for x in range(1,11) if x % 2 == 0]
print(res)

# 使用两层循环，可以生成全排列
res = [m + n for m in 'ABC' for n in '123']
print(res)

# 列出上一层目录下的所有文件和目录名
res = [d for d in os.listdir('../')]
print(res)

# for 循环可以同时使用多个参数
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k,'=>',v)

#　列表也可以使用多个参数
res = [k + '=' + v for k, v in d.items()]
print(res)
```

> 写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把list创建出来



### 生成器（generator）

创建一个generator，第一种方法很简单，只要把一个列表生成式的`[]`改成`()`，就创建了一个generator：

```python
l = [x * x for x in range(10)]
print(l)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
print(g)

#通过 next() 函数获得generator的下一个返回值：
print(next(g)) # 0
print(next(g)) # 1

# 一般通过 for 循环
for i in g:
    print(i)
```

创建 l  和g 的区别仅在于最外层的 [] 和 () ，l 是一个list，而 g 是一个generator。



例：斐波拉契数列（Fibonacci）

```python
def fibnc(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done !'
```

注意，赋值语句：

```python
a, b = b, a + b
```

相当于：

```python
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
```

但不必显式写出临时变量t就可以赋值。

第二种方法：函数定义中包含 yield 关键字，那么这个函数就是一个generator。

> 函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用 next() 的时候执行，遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行。

是用 for 循环调用 generator 时，如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中。



### 迭代器

可以直接作用于 for 循环的数据类型：一类是集合数据类型，list, tuple, dict, set, str等。一类是 generatoe。这些对象统称为可迭代对象 Iterable 。

```python
from collections import Iterable
isinstance([], Iterable) # True
isinstance(90, Iterable) # False
```

可以被 next() 函数调用并不断返回下一个值的对象称为迭代器：Iterator。可以使用 isinstance() 判断一个对象是否是 Iterator 对象。

> Iterator 的计算是惰性的，只有在需要返回下一个数据时它才会计算。



## 函数式编程（Functional Programming）

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。



### 高阶函数

####Google 论文 《[MapReduce: Simplified Data Processing on Large Clusters][3]》

-- Jeffrey Dean and Sanjay Ghemawat

> 和诸多语言的思想一样，高度抽象的编程范式

- 变量可以指向函数
- 函数名也可以是变量
- 一个函数作为另一个函数的参数


#### map 和 reduce



#### filter

从一个序列中筛出符合条件的元素



#### sorted

- 直接使用可以对 list  排序

  ```python
  sorted([1,3,44,2,3,4,5,])
  ```

- 也是一个高阶函数，用作自定义排序



### 返回函数

#### 函数作为返回值

把函数作为结果返回。

比如一个简单的求和：

```python
def calc_sum(*args):
    x = 0
    for i in args:
        x = x + i
    return x
```

> 这里的 * 意思是传进来的位置参数都装在元组 args 里，** 代表字典参数，下同
>
> calc_sum(\*args)，调用时，* 的意思是把序列中的每个元素当作位置参数穿进去

但如果不需要立即求和，而是在需要的时候在计算：

```python
def lazy_sum(*args):
    def sum():
      x = 0
      for i in args:
          x = x + i
      return x
    return sum
```

返回求和函数，调用时才是真正计算：

```python
f = lazy_sum(1,2,3,4,333)
f() # 此时才进行计算
```

> 当返回 sum 时候，相关的参数和变量都保存在返回函数中，称 闭包 。

#### 闭包

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

### 匿名函数

略

### 装饰器

函数对象有一个 `__name__` 属性时，可以得到函数的名字

```python
def now():
    print('2017-1-12')
f = now
f() # 2017...
f.__name__ # now
```

现在要增强 now 函数的功能，但又不希望修改 now 函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。装饰器可以理解为一个返回函数的高阶函数。

```python
# 打印日志的方法
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

> *args, **kw 表示接受任意参数的调用

借助Python的@语法，把decorator置于函数的定义处：

```python
@log
def now():
    print('2017-1-12')
    
now() # call now() 2017-1-12
```

把 @log 放到 now 函数的定义处，相当于执行了语句：

```python
now = log(now)
```

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

```python
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
now.__name__ #　wrapper
```

函数也是对象，但经过 decotator 装饰之后的函数， `__name__`  已经变为了 wrapper。因为返回的那个 wrapper() 函数名字就是 wrapper ，所以，需要把原始函数的`__name__`等属性复制到 wrapper() 函数中，否则，有些依赖函数签名的代码执行就会出错。

用 Python内置的 functools.wraps 来处理，所以，一个完整的decorator的写法如下：

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

### 偏函数

Python的 functools 模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。

比如 int 有一个参数：

```python
int('1112', base=8) # base 的默认值为10， 进行 N 进制的转换
```

假设要大量转 2 进制：

```python
def int2(x, base=2):
    return int(x, base)
```

functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定义 int2()：

```python
import functools
int2 = functools.partial(int, base=2)
```

简单说， functools.partial 就是把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。



## 模块

类比 PHP 的组件。在Python中，一个.py文件就称之为一个模块（Module）。



为了避免模块名冲突，Python引入了按目录来组织模块的方法，称为包（Package）:

```python
--test_pack
----__init__.py
----aa.py
----bb.py
```

> 每一个包目录下面都会有一个 `__init__.py` 的文件，这个文件是必须存在的，否则，Python 就把这个目录当成普通目录，而不是一个包。`__init__.py` 可以是空文件，也可以有 Python 代码，因为`__init__.py`本身就是一个模块，而它的模块名就是 mycompany。

aa.py 的模块名就是：test_pack.aa

> 不能和Python自带的模块名称冲突：比如自带 sys ，os



### 使用模块

Python模块的标准文件模板：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' #　任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'zuozhe'　# 作者

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```

在运行模块时，Python 解释器把一个特殊变量`__name__`置为`__main__`，而如果在其他地方导入该模块时，if 判断将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。



#### 作用域

Python中，是通过 _ 前缀来实现的。

正常的函数和变量名是公开的（public），可以被直接引用。

类似`__xxx__`这样的变量是特殊变量，可以被直接引用，但是有特殊用途。

类似`_xxx`和`__xxx`这样的函数或变量就是非公开的（private）。

```python
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

### 第三方模块

在Python中，安装第三方模块，是通过包管理工具pip完成的。

Mac或Linux，pip 已经安装。Win 环境需要在安装时勾选。

> Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是`pip3`。

同 PHP 的组件一样，Python 的模块在：[pipi.python][3]

例如，安装 Python 的图像处理工具库，Pillow（基于Python Imaging Library，支持 Python3）。

```python
pip install Pillow
```

生成一个缩略图

```python
from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode) # PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
```

其他常用的第三方库还有MySQL的驱动：`mysql-connector-python`，用于科学计算的NumPy库：`numpy`，用于生成文本的模板工具`Jinja2`，等等。

#### 模块搜索路径

Python会在指定的路径下搜索对应的.py文件，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在`sys`模块的`path`变量中：

```python
import sys
sys.path

# 添加自己的搜索目录
import sys
sys.path.append('/Users/xxx/my_py')
```



## 面向对象

在 Python 中，所有数据类型都可以视为对象。

### 类和实例

首先写一个 Python 格式的 class：

```python
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_score(self):
        print('s%: s%' % (self.name, self.score))
       
susan = Student('susan', 99)
susan.get_score()
```

class 后面紧跟类名，类名通常大写开头，（object）表示该类是从哪个类继承下来的，若没有就写 object 类，这是所有类最终都会继承的类。创建实例，通过类名+（） 实现。

`__init__`方法的第一个参数永远是 self ，表示创建的实例本身，然后在self 上绑定参数，有了这个方法，在创建实例的时候就不能传入空参数。

### 访问限制

Student 类，外部代码还是可以修改实例的 name，score 属性，如果要让内部属性不被访问，需要在属性名称前加上两个下划线：

```python
class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def get_score(self):
        print('s%: s%' % (self.__name, self.__score))
       
susan = Student('susan', 99)
print(susan._Student__name) #仍然可以访问
susan.__name
```

> 实例的变量名如果以`__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量。但是不同版本的Python解释器可能会把`__name`改成不同的变量名，所以不可以这么做。

如果外部代码要获取name和score，可以给Student类增加 get_name 和 get_score 方法，修改增加 set_name，set_score 方法，在方法内可以进行参数验证。

> 在Python中，变量名类似`__xxx__`的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用`__name__`、`__score__`这样的变量名。类似`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”



### 继承和多态

当子类和父类都存在相同的 run() 方法时，我们说，子类的 run() 覆盖了父类的 run() ，在代码运行的时候，总是会调用子类的 run()。这样，我们就获得了继承的另一个好处：多态。

### 获取对象信息

type() 方法：

```python
type(123) # <class 'int'>

#判断一个对象是否是函数
import types

def fn():
    pass

print(type(fn)==types.FunctionType)
```

对于class的继承关系来说，使用 type() 就很不方便。我们要判断class的类型，可以使用 isinstance()函数。

```python
#继承关系：
object -> Animal -> Dog -> Husky
h = Husky()
isinstance(h, Husky) # True
isinstance(h, Dog) # True

```

dir() 方法，获取一个对象的所有属性和方法，

```python
print(dir('aa'))
```

类似`__xxx__`的属性和方法在Python中都是有特殊用途的，比如`__len__`方法返回长度。在 Python中，如果你调用 len() 函数获取一个对象的长度，实际上，在 len() 函数内部，它自动去调用该对象的`__len__()`方法，所以，下面的代码是等价的：

```python
len('ABC') # 3
'ABC'.__len__() # 3
```



### 实例属性和类

给实例绑定属性的方法是通过实例变量，但是，如果 Student 类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归 Student 类所有：

```python
class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name) # Student, 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性

print(Student.name) # Student,打印类的name属性

s.name = 'Michael' # 给实例绑定name属性
print(s.name) # Michael,由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性

print(Student.name) # Student,但是类属性并未消失，用Student.name仍然可以访问

del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
```



## 面向对象高级编程

在Python中，面向对象还有很多高级特性。

### 使用`__slots__`

正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法。

```python
from types import MethodType

class Student(object):
    pass
s = Student()
s.name = 'susan' # 动态给实例绑定一个属性
print(s.name) # susan

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 25
```

此时绑定发方法只对此实例有效。为了给所有实例都绑定方法，可以给class绑定方法：

```python
def set_score(self, score):
    self.score = score

Student.set_score = set_score
```

只允许对Student实例添加 name 和 age 属性。为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
  
s = Student()
s.name = 'susan'
s.age = 25
s.score = 99
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'
```

> 使用`__slots__`要注意，`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的



### 使用 @propety

Python内置的 @property 装饰器就是负责把一个方法变成属性调用的：

```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

> @property 的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上 @property 就可以了，此时， @property 本身又创建了另一个装饰器 @score.setter ，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作。



### 多重继承

通过多重继承，一个子类就可以同时获得多个父类的所有功能。

```python
class Bat(Mammal, Flyable):
    pass
```

> 两个父类中有相同方法，子类调用这个方法时， 调用的是第一个被继承父类的方法

#### Mixln

这种设计通常称之为 MixIn。MixIn 的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个 MixIn 的功能，而不是设计多层次的复杂的继承关系。

### 定制类

`__len__()`方法是为了能让class作用于 len() 函数。

`__str__()`方法定制打印内容。

`__repr__()`交互环境下调试服务使用。

`__iter__()`方法用于 for 循环。

`__getitem__()`方法用于像 list 那样按照下标取出元素。切片功能要单独写，一个切片对象 slice。

`__getattr__()`方法，动态返回一个属性。

> 这个方法的应用场景：可以写出一个链式调用，见 demo。

`__call__()`方法，可以直接对实例进行调用。

> 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
>
> 通过 callable() 函数，我们就可以判断一个对象是否是“可调用”对象。



### 使用枚举类

```python
from enum import Enum, unique

@unique # 保证没有重复值的成员
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7

c = Color
print(Color['red']) #Color.red
print(Color['red'].name) # red
print(Color['red'].value) # 1

# 每一个成员都有它们各自名称和值，Color.red成员的名称是：red，值是：1。
```



### 使用元类

type() 函数可以查看一个类型或变量的类型，也可以创建新的类型。

```python
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

print(type(Hello)) # <class 'type'>
```



要创建一个 class 对象， type() 函数依次传入3个参数：

- class 的名称；
- 继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，别忘了 tuple 的单元素写法；
- class的方法名称与函数绑定，这里我们把函数 fn 绑定到方法名 hello 上。

#### metaclass (元类)

除了使用 type() 动态创建类以外，要控制类的创建行为，还可以使用 metaclass。

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

待定---



# 错误，调试和测试

### 错误处理

```python
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```

出现错误先执行 except ，再执行 finally ，没有错误，finally 也被执行

#### 调用堆栈

如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。

#### 记录堆栈

Python 内置的 logging 模块可以非常容易地记录错误信息：

```python
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
```

通过配置，logging 还可以把错误记录到日志文件里，方便事后排查。

#### 抛出错误

因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。



### 调试

- 直接 print 简单粗暴有效，当然无脑 print 就算了
- 凡是用 print 来辅助查看的地方，都可以用断言（assert）来替代：

````python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
````

- 把 print 替换为 logging 是第3种方式，和 assert 比，logging 不会抛出错误，而且可以输出到文件：

```python
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```

- 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

```python
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')


s = '0'
n = int(s)
print(10 / n)

# 命令行
python3 -m pdb err.py
#然后输入 1 来查看代码 这里有点问题，
```



### 单元测试

测试驱动开发（TDD：Test-Driven Development）。测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。mydict.py:

```python
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
```

引入Python自带的 unittest 模块，编写 mydict_test.py 如下：

```python
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertEqual(isinstance(d, dict))
       
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
        
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
       
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
          
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
     
    if __name__ == '__main__':
        unittest.main()
```

编写单元测试时，需要编写一个测试类，从 unittest.TestCase 继承。

以 test 开头的方法就是测试方法，不以 test 开头的方法不被认为是测试方法，测试的时候不会被执行。对每一类测试都需要编写一个 test_xxx() 方法。由于 unittest.TestCase 提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是 assertEqual()：

```python
self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
```

另一种重要的断言就是期待抛出指定类型的 Error，比如通过 d['empty'] 访问不存在的key时，断言会抛出 KeyError ：

```python
with self.assertRaises(KeyError):
    value = d['empty']
```

而通过 d.empty 访问不存在的 key 时，我们期待抛出 AttributeError ：

```python
with self.assertRaises(AttributeError):
    value = d.empty
```

运行单元测试：

```python
python3 mydict_test.py
```

或者

```python
python3 -m unittest mydict_test
```

#### setUP 与 tearDown

这两个方法会分别在每调用一个测试方法的前后分别被执行。



### 文档测试

Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用 ... 表示中间一大段烦人的输出。

```python
# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
```

运行：

```python
python3 mydict2.py
```

什么输出也没有。这说明我们编写的doctest运行都是正确的。



## IO 编程

使用了流（stream）概念，每种语言都有这个。

同步和异步。

异步的编程模型复杂，涉及到怎么通知，回调模式（程序执行完来告诉你），轮询模式（不停的查询程序执行完没有）等。



### 文件读写

```python
f = open('/xx/xx/test.txt', 'r') # r 表示读
f.read() # 一次性读取全部内容 

f.close()
```

> Python把内容读到内存，用一个`str`对象表示

由于文件读写可能产生 IOError ，一旦出错 close() 不会被调用，Python 引入了 with 语句来自动调用 close

```python
with open('/xx/xx/file', 'r') as f:
    print(f.read()) 
```

针对大型文件

反复调用 read(size) 方法，每次最多读取 size 个字节的数据。

调用 readline() 可以每次读取一行内容，调用 readlines() 一次读取所有内容并按行返回 list 。

```python
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

#### file-like Object

像 open() 函数返回的这种有个 read() 方法的对象，在 Python 中统称为 file-like Object。除了 file 外，还可以是内存的字节流，网络流，自定义流等等。file-like Object 不要求从特定类继承，只要写个 read() 方法就行。

 StringIO 就是在内存中创建的file-like Object，常用作临时缓冲。

#### 二进制文件

要读取二进制文件，比如图片、视频等等，用 rb 模式打开文件即可：

```python
f = open('/xx/xx/test.jpg', 'rb')
f.read()
# b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

#### 字符编码

要读取非UTF-8编码的文本文件，需要给 open() 函数传入 encoding 参数，例如，读取 GBK 编码的文件：

```python
f = open('/xx/xx/gbk.txt', 'r', encoding='gbk')
f.read()
```

遇到有些编码不规范的文件，你可能会遇到 UnicodeDecodeError ，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况， open() 函数还接收一个 errors 参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```python
f = open('/xx/xx/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

#### 写文件

写文件和读文件是一样的，唯一区别是调用 open() 函数时，传入标识符 'w' 或者 'wb' 表示写文本文件或写二进制文件：

```python
f = open('/xx/xx/test.txt', 'w')
f.write('Hello, world!')
f.close()
```

你可以反复调用 write() 来写入文件，但是务必要调用 f.close() 来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用 close() 方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用 close() 的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用 with 语句来得保险：

```python
with open('/x/xx/test.txt', 'w') as f:
    f.write('Hello, world!')
```

要写入特定编码的文本文件，请给 open() 函数传入 encoding 参数，将字符串自动转换成指定编码。













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



Windows 环境下 Windows把反斜杠（\）作为目录分隔符，而Python用反斜杠表示转义符！ 所以，你得使用转义符来表示反斜杠本身或者使用自然字符串。例如，使用'C:\\Documents'或r'C:\Documents'而不是'C:\Documents'——你在使用一个不知名的转义符\D！



[1]:https://docs.python.org/3/
[2]:http://baike.baidu.com/item/%E6%B1%89%E8%AF%BA%E5%A1%94/3468295
[3]:https://research.google.com/archive/mapreduce.html
[4]:https://pypi.python.org/