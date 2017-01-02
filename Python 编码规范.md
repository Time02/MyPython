# Python 编码规范

  目前网上的许多版本的编码规范都是遵循 PEP8 点规范：

- [PEP 0008-Style Guide for Python Code][0]
- [Google 的风格指南][1]
- [Python Guide - Code Style][2]
- [Pocoo Styleguide][3]

除了主动遵循规范，还可以借助工具，格式化代码：

- IntelliJ IDEA 和 PyCharm 的格式化代码功能。
- Google 开源的 Python 文件格式化工具：[yapf][4]。
- [pyflakes][5], [pylint][6] 等工具。

##代码布局 （Code lay-out）

###缩进（Indentation）
4 个空格，Python 3 不允许将tab和空格键混合使用用于缩进

```python
#对齐
#使用分隔符来对齐
foo - long_function_name(var_one, var_two,
                         var_three, var_four)

#使用额外的缩进，与其他缩进区分开
def long_function_name(
        var_one, var_two, var_three,
        var_four);
    print(var_one)

# 悬挂式缩进应该增加一个级别。悬挂式缩进的空格个数【可以】不为4。
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

if 语句

```python
# 没有多余缩进
if (this_is_one_thing and
    that_is_another_thing):
    do_something()
    
# 在条件判断语句所在行添加一些额外的缩进
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

括号：在多行代码结构中，括号可以排在列出元素最后一行的第一个非空字的下面，或者排在多行代码结构起始的第一个字符下面

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

###行最大长度（Maximum Line Length）

限制最大长度为 79 个字符，（其实可以参考 PHP 每行不超过 80，至少不超过200）

长代码折行：可以使用反斜杠来续行，\

###空行（Blank Lines）

使用两行空行分隔顶层函数和类的定义。使用单行空行分隔类方法定义。

###编码（Source File Encoding）

始终使用 UTF-8

###导入（import）

- 使用单独的行，必须声明在文件顶部， 在文档申明之后，全局变量之前。
- imports应分组顺序：1. 标准库 2. 相关的第三方库 3. 本地应用程序/库
- 你应该把各组的imports之间留一个空行。 
- __all__申明放在最后。
- 通配符imports（ from <module> import *）应该避免使用。

###表达式和语句中的空格（Whitespace in Expressions and Statements ）

```python
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )

Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x

Yes:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

No:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]


Yes: spam(1)
No:  spam (1)

Yes: dct['key'] = lst[index]
No:  dct ['key'] = lst [index]

Yes:
x = 1
y = 2
long_variable = 3

No:
x             = 1
y             = 2
long_variable = 3

```

###其他建议（Other Recommendations）
- 在这些二元运算符前后加一个空格：赋值（=），自增赋值（+=，-= 等等）， 比较（==，<，>，!=，<>，<=，>=，in，not in，is，is not)，布尔运算（and，or，not）。
- 不同优先级的运算符，在最低优先级的操作符前后添加空格，
- 不要在一个关键字参数或者一个缺省参数值的 = 符号前后加一个空格。
- 通常不推荐使用复合语句（一行代码中有多条语句）。

###注释（Comments）

当代码变化时始终优先更新注释！ 

###块注释（Block Comments）

块注释在一些（或全部）代码之前，并和代码缩进一致。每行注释均以#开头，然后紧跟一个空格（除非在注释内缩进）。

块注释内的段落使用仅含 # 的单行分隔。

###行内注释（Inline Comments）

谨慎地使用内嵌注释。 
内嵌注释是一种和语句在同一行的注释。内嵌注释至少和语句间隔2个空格。他们开始于一个#和一个空格。 如果语句显而易见，
那么内嵌注释是不必要的。

###文档字符串（Documentation Strings）

编写良好的文档字符串，约定永远在PEP257更新文档字符串风格说明。 

所有的公共模块，函数，类和方法都需要编写文档字符串。

```python
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```

###版本注记（Version Bookkeeping）

如果在源代码文件中掺杂着 Subversion，CVS，RCS 注记，按照一下规则写。

```python
__version__ = "$Revision: e222222 $"
# $Soures$
```

##命名约定

Python 库的命名约定优点乱，未达成一致，但是有一些推荐的标准。

###首要原则（Overriding Principle）

API 的接口名字应该反映使用法方法而不是具体的实现过程。

###描述：命名风格（Descriptive: Naming Styles）

文档不益于理解，等熟悉 Python 后再补充。

##说明：命名规范（Prescriptive: Naming Conventions）

###需要避免的命名(Names To Avoid)

避免使用‘l’（小写的L），‘O’（大写的o），‘I’（大写的i）

###包和模块命名(Package And Module Names)

模块使用简短，全小写的名字，下划线增强可读性。

Python 的包也是全小写，短名称，不建议下划线，因为模块名和文件名关联，而且某些文件系统大小写不敏感，会截断过长的名字

###类命名(Class Names)

类命名应该使用单词字母大写（CapWords）的命名约定。

当接口已有文档说明且主要是被用作调用时，也可以使用函数的命名约定。

注意对于内建命名(builtin names)有一个特殊的约定：大部分内建名都是一个单词（或者两个一起使用的单词），单词首字母大写(CapWords)的约定只对异常命名和内建常量使用。

###异常命名(Exception Names)

由于异常实际上也是类，因此类命名约定也适用与异常。不同的是，如果异常实际上是抛出错误的话，异常名前应该加上”Error”的前缀。

###全局变量命名(Global Variable Names)

（在此之前，我们先假定这些变量都仅在同一个模块内使用。）这些约定同样也适用于函数命名。

对于引用方式设计为from M import *的模块，应该使用__all__机制来避免import全局变量，或者采用下划线前缀的旧约定来命名全局变量，从而表明这些变量是“模块非公开的”。


###函数命名(Function Names)

函数命名应该都是小写，必要时使用下划线来提高可读性。

只有当已有代码风格已经是混合大小写时（比如threading.py），为了保留向后兼容性才使用混合大小写。

###函数和方法参数(Function And Method Arguments)

实例方法的第一参数永远都是self。

类方法的第一个参数永远都是cls。

在函数参数名和保留关键字冲突时，相对于使用缩写或拼写简化，使用以下划线结尾的命名一般更好。比如，class_比clss更好。（或许使用同义词避免这样的冲突是更好的方式。）

###方法命名和实例变量(Method Names And Instance Variables)

使用函数命名的规则：小写单词，必要时使用下划线分开以提高可读性。

仅对于非公开方法和变量命名在开头使用一个下划线。

避免和子类的命名冲突，使用两个下划线开头来触发Python的命名修饰机制。

Python类名的命名修饰规则：如果类Foo有一个属性叫__a，不能使用Foo.__a的方式访问该变量。（有用户可能仍然坚持使用Foo._Foo__a的方法访问。）一般来说，两个下划线开头的命名方法只应该用来避免设计为子类的属性中的命名冲突。

###常量(Constants)

MAX_OVERFLOW and TOTAL. 常量通常是在模块级别定义的，使用全部大写并用下划线将单词分开。例如：MAX_OVERFLOW和TOTAL

###继承的设计(Designing For Inheritance)

记得永远区别类的方法和实例变量（属性）应该是公开的还是非公开的。如果有疑虑的话，请选择非公开的；因为之后将非公开属性变为公开属性要容易些。

公开属性是那些和你希望和你定义的类无关的客户来使用的，并且确保不会出现向后不兼容的问题。非公开属性是那些不希望被第三方使用的部分，你可以不用保证非公开属性不会变化或被移除。

我们在这里没有使用“私有（private）”这个词，因为在Python里没有什么属性是真正私有的（这样设计省略了大量不必要的工作）。

另一类属性属于子类API的一部分（在其他语言中经常被称为”protected”）。一些类是为继承设计的，要么扩展要么修改类行为的部分。当设计这样的类时，需要谨慎明确地决定哪些属性是公开的，哪些属于子类API，哪些真的只会被你的基类调用。

Python风格的指南：

- 公开属性不应该有开头下划线。
- 如果公开属性的名字和保留关键字有冲突，在你的属性名尾部加上一个下划线。这比采用缩写和简写更好。（然而，和这条规则冲突的是，‘cls’对任何变量和参数来说都是一个更好地拼写，因为大家都知道这表示class，特别是在类方法的第一个参数里。）
- 对于简单的公共数据属性，最后仅公开属性名字，不要公开复杂的调用或设值方法。记住在Python中，提供了一条简单的路径来实现未来增强，你应该简单数据属性需要增加功能行为。这种情况下，使用 properties 将功能实现隐藏在简单数据属性访问语法之后。
- 如果你的类是子类的话，你有一些属性并不想让子类访问，考虑将他们命名为两个下划线开头并且结尾处没有下划线。这样会触发Python命名修饰算法，类名会被修饰添加到属性名中。这样可以避免属性命名冲突，以免子类会不经意间包含相同的命名。

###公开和内部接口(Public And Internal Interfaces)

任何向后兼容性保证仅对公开接口适用。相应地，用户能够清楚分辨公开接口和内部接口是很重要的。

文档化的接口被认为是公开的，除非文档中明确申明了它们是临时的或者内部接口，不保证向后兼容性。所有文档中未提到的接口应该被认为是内部的。

为了更好审视公开接口和内部接口，模块应该在__all属性中明确申明公开API是哪些。将__all__设为空list表示该模块中没有公开API。

即使正确设置了__all属性，内部接口（包，模块，类，函数，属性或其他命名）也应该以一个下划线开头。

如果接口的任一一个命名空间（包，模块或类）是内部的，那么该接口也应该是内部的。

导入的命名应该永远被认为是实现细节。其他模块不应当依赖这些非直接访问的导入命名，除非它们在文档中明确地被写为模块的API，例如os.path或者包的__init__模块，那些从子模块展现的功能。

















[0]:[https://www.python.org/dev/peps/pep-0008/]
[1]:[http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/]
[2]:[http://docs.python-guide.org/en/latest/writing/style/]
[3]:[http://flask.pocoo.org/docs/0.10/styleguide/]
[4]:[github.com/google/yapf]
[5]:[https://github.com/PyCQA/pyflakes]
[6]:[https://www.pylint.org/]