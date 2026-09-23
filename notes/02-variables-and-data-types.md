# 2 变量和简单数据类型

> 包含视频：`2 先导篇：打印`（06:26）、`更多打印`（06:43）、`2.2 变量（上/下）`、`2.3 字符串`（05:35）、`2.4 数`（05:22）、`2.5 注释`（04:08）、`2 番外篇：数据类型`（06:59）

## 2 先导篇：打印 `print()`

`print()` 把内容输出到屏幕，是 Python 里第一个也是最常用的函数。

```python
print("Hello Python world!")
print('单引号也行')
print("混合\"引号\"要转义")   # 反斜杠转义
print('里面放 "双引号" 就别转义')
```

### `print()` 的两个实用参数

```python
print("A", "B", "C")                 # 默认用空格分隔 → A B C
print("A", "B", sep="-")             # sep 改分隔符 → A-B-C
print("第一行", end="")               # end 改行尾，默认是 \n
print("接在同一行")
```

### 一次打印多行：三引号

```python
print("""line1
line2
line3""")
```

> 三引号包起来的字符串会保留换行，也常被当作**多行注释**用（其实它是字符串字面量）。

## 2 先导篇（二）：更多打印

打印有 4 种常见玩法，从"能用"到"好用"排序：**`+` 拼接 → f-string 格式化 → 引号/转义 → `sep`/`end` 控格式**。

### ① 用 `+` 拼接字符串

`+` 把两段字符串接在一起，**不会自动加空格**，空格要自己写：

```python
print("Hello" + "Python")          # HelloPython   ← 粘一起了
print("Hello" + " " + "Python")    # Hello Python  ← 空格自己加

first_name = "ada"
last_name = "lovelace"
print("Hello, " + first_name + " " + last_name + "!")   # Hello, ada lovelace!
```

> ⚠️ `+` **只能拼字符串 + 字符串**。要拼数字必须先 `str()` 转成字符串，见下面 ③。

### ② 格式化打印：引号前面加一个 `f`（f-string）

在引号前面写一个 **`f`**（大写 `F` 也行），字符串里用 `{}` 放变量，Python 自动帮你塞进去并转成字符串：

```python
name = "ada"
age = 18
price = 3.14159

print(f"我叫{name}，今年{age}岁")       # 我叫ada，今年18岁
print(f"明年我{age + 1}岁")             # {} 里可以直接运算
print(f"{name.title()}")                # {} 里可以直接调方法
print(f"价格：{price:.2f}")             # :.2f 保留两位小数 → 价格：3.14
print(f"{{字面大括号}}")                 # 真要打印 {} 就写两个
```

三种写法对比：

| 写法 | 例子 | 评价 |
|------|------|------|
| `+` 拼接 | `"年龄：" + str(age)` | 变量一多就一坨，还容易漏 `str()` |
| **f-string** | `f"年龄：{age}"` | ✅ **第 3 版主力写法，首选** |
| `%` / `format()` | `"年龄：%d" % age`、`"年龄：{}".format(age)` | 老写法，看得懂就行，别主动写 |

> 记忆口诀：**引号前面加个 f，变量往 {} 里面堆。**

### ③ 数字要拼进字符串打印，必须转成 string

```python
age = 18
print("我今年" + age)          # ❌ TypeError: can only concatenate str to str
print("我今年" + str(age))     # ✅ 手动 str() 转换
print(f"我今年{age}")          # ✅ f-string 自动转换（推荐）

# 反过来：字符串数字要拿来算，也要转
num = int("42") + 1            # 43
```

常见类型转换：`str(x)` 转字符串、`int(x)` 转整数、`float(x)` 转小数。

### ④ 引号的用法

```python
print("双引号")
print('单引号')                 # 两者完全等价，选一种全程统一

print('外面单引号，里面放 "双引号" 不用转义')
print("外面双引号，里面放 '单引号' 不用转义")
print("外面双引号，里面还要\"双引号\"就得转义")

print("""三引号可以
直接换行写""")
```

一句话规则：**外双内单、外单内双**，实在撞车了就用 `\` 转义。

### ⑤ 转义符号 `\`（反斜杠）

反斜杠告诉 Python："后面这个字符按特殊意思处理"。

| 转义 | 作用 | 例子 |
|------|------|------|
| `\n` | 换行 | `print("a\nb")` → 两行 |
| `\t` | 制表符（Tab 缩进） | `print("a\tb")` |
| `\\` | 打印一个真正的反斜杠 | `print("C:\\Users")` → `C:\Users` |
| `\"` `\'` | 打印引号本身 | `print("他说\"你好\"")` |
| `\r` | 回车（光标回到行首） | 进度条常用 |

```python
print("第一行\n第二行")
print("路径：C:\\Users\\me")      # 不写两个斜杠会被当成转义符
print(r"C:\Users\me")             # 原始字符串 r""：里面所有 \ 都不转义
```

## 2.2 变量（上）：变量是什么

变量 = **贴在值上的标签**。Python 是动态类型，变量不需要声明类型。

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"   # 重新赋值
print(message)      # 只保留最新值
```

### 命名规则（红线）

| 规则 | 例子 |
|------|------|
| 只能用字母、数字、下划线 | ✅ `message_1` ❌ `1_message` |
| 不能有空格（用下划线分隔） | ✅ `student_name` ❌ `student name` |
| 不能用关键字/函数名 | ❌ `print`、`class`、`list` |
| 区分大小写 | `Name` ≠ `name` |
| 别用 `l` 和 `O` | 容易被看成 `1` 和 `0` |

### 一行给多个变量赋值

```python
x, y, z = 0, 0, 0
a = b = 100          # 同一个值赋给多个变量
x, y = y, x          # 交换两个变量（Python 特色写法）
```

> ⚠️ 变量必须先赋值再使用，否则 `NameError: name 'xxx' is not defined`。

## 2.2 变量（下）：命名习惯与调试

### 三种命名法（认全，别混着用）

| 命名法 | 写法 | 例子 | 在 Python 里用在哪 |
|--------|------|------|-------------------|
| **下划线法** snake_case | 全小写，单词之间用 `_` 连接 | `user_name`、`max_score` | ✅ **变量、函数名的首选（Python 官方风格）** |
| 小驼峰 camelCase | 第一个词小写，后面每个词首字母大写 | `userName`、`maxScore` | ⚠️ Python 里不推荐（Java / JS 的风格），但要认得 |
| 大驼峰 PascalCase | 每个词首字母都大写 | `UserName`、`StudentInfo` | ✅ **类名**用这个 |

```python
# ✅ Python 的标准长相：变量/函数下划线法，类名大驼峰
student_name = "张三"

def get_student_name():     # 函数：下划线法
    return student_name

class StudentInfo:          # 类：大驼峰
    pass
```

> 本笔记全程用**下划线法**。看到别人的 `userName` 别以为是错的，只是语言习惯不同。
> 常量另算：**全大写 + 下划线**，如 `MAX_CONNECTIONS = 5000`。

### 名字不能撞关键字（红线）

Python 有 35 个保留关键字，拿来当变量名直接 `SyntaxError`：

```
False  None  True  and  as  assert  async  await  break  class  continue
def  del  elif  else  except  finally  for  from  global  if  import  in
is  lambda  nonlocal  not  or  pass  raise  return  try  while  with  yield
```

```python
class = "三班"        # ❌ SyntaxError: invalid syntax
for = 5               # ❌ SyntaxError
list = [1, 2, 3]      # ❌ 语法上能跑，但把内置函数 list() 覆盖了，后面必炸
print = 1             # ❌ 同理，print() 从此报废
```

拿不准某个名字能不能用，直接问解释器：

```python
import keyword
keyword.iskeyword("class")   # True  ← 是关键字，不能当变量名
keyword.kwlist               # 打印出全部关键字
```

> 判断小技巧：PyCharm 里**自动变色（蓝色/紫色）的单词**，基本都是关键字或内置名，别拿它当变量名。

### 起名要有描述性

- `name` 优于 `n`，`student_name` 优于 `s_n`
- 布尔变量用 `is_xxx` / `has_xxx` / `can_xxx`，如 `is_running`

### 三个经典错误类型：

```python
# 1. 语法错误 SyntaxError —— 漏括号/引号，程序一行都跑不起来
print("hello"        # SyntaxError: '(' was never closed

# 2. 名称错误 NameError —— 用了没定义的变量，或拼写不一致
mesage = "hi"
print(message)       # NameError: name 'message' is not defined

# 3. 类型错误 TypeError —— 类型不匹配
age = 18
print("我今年" + age)  # TypeError: can only concatenate str to str
```

**读报错的正确姿势：从最后一行往上读**，最后一行告诉你"错在哪、为什么"。

## 2.3 字符串

字符串就是一串字符，用引号包起来。

### 修改大小写（不改变原变量，返回新字符串）

```python
name = "ada lovelace"
print(name.title())    # Ada Lovelace   每个单词首字母大写
print(name.upper())    # ADA LOVELACE
print(name.lower())    # ada lovelace
```

### f-string：字符串里插变量（第 3 版主力写法）

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
# Hello, Ada Lovelace!

# 大括号里可以直接运算、调方法
print(f"2 + 3 = {2 + 3}")
print(f"{name.upper()} 今年 {20 + 1} 岁")
```

> 老写法 `format()` 和 `%` 已不推荐，认准 **`f""`**。

### 空白：制表符与换行

```python
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# \n 换行，\t 制表符（相当于 Tab）
```

### 删除空白（处理用户输入必用）

```python
s = "  python  "
print(s.rstrip())   # "  python"   删右边
print(s.lstrip())   # "python  "   删左边
print(s.strip())    # "python"     删两边
```

> ⚠️ `strip()` **返回新字符串**，不修改原变量。要永久去掉必须回写：`s = s.strip()`。

### 第 3 版新增：`removeprefix()` / `removesuffix()`

```python
url = "https://nostarch.com"
print(url.removeprefix("https://"))   # nostarch.com

file_name = "python_notes.txt"
print(file_name.removesuffix(".txt")) # python_notes
```

比手写切片安全：前缀不存在时**原样返回**，不会切坏。

### 其他常用字符串方法

```python
"python".replace("p", "P")        # Python
"a,b,c".split(",")                # ['a', 'b', 'c']  字符串 → 列表
"-".join(["a", "b", "c"])         # a-b-c            列表 → 字符串
"python" in "I love python"       # True             包含判断
len("python")                     # 6                长度
"python".find("th")               # 2                找不到返回 -1
"abc".startswith("a")             # True
```

## 2.4 数

### 整数 `int`

```python
print(2 + 3)      # 5   加
print(10 - 3)     # 7   减
print(3 * 4)      # 12  乘
print(7 / 2)      # 3.5 除，结果永远是 float
print(7 // 2)     # 3   整除（向下取整）
print(7 % 2)      # 1   取余（判断奇偶神器）
print(2 ** 10)    # 1024 乘方
```

运算优先级：`**` > `* / // %` > `+ -`，不确定就加括号：

```python
print((2 + 3) * 4)   # 20
```

### 浮点数 `float`

```python
print(0.1 + 0.2)        # 0.30000000000000004  ← 二进制精度问题
print(round(0.1 + 0.2, 2))   # 0.3   用 round() 控制位数
```

> 涉及钱的计算用 `decimal` 模块，别用 float。

### 数 + 字符串

```python
age = 23
print(f"Happy {age}rd Birthday!")     # ✅ f-string 自动转（推荐）
print("Happy " + str(age) + "rd Birthday!")  # ✅ 手动 str()
print("Happy " + age + "rd Birthday!")       # ❌ TypeError
```

### 常量

Python 没有真常量，约定用**全大写**表示"别改它"：

```python
MAX_CONNECTIONS = 5000
```

### 下划线可读性（Python 3.6+）

```python
universe_age = 14_000_000_000    # 等价于 14000000000，只是好看
print(universe_age)              # 14000000000
```

## 2.5 注释

### 注释的分类（4 类，按用法选）

| 分类 | 写法 | 什么时候用 |
|------|------|-----------|
| 单行注释 | `# 说明` | 只解释**一行**代码「为什么这么做」 |
| 行内注释 | `code  # 说明` | 紧跟在代码右边，能不写就不写 |
| **多行注释** | `""" 说明 """`（三引号） | **注释内容超过一行时，一律用多行注释**，不要一行一个 `#` |
| 文档字符串 docstring | 函数 / 类 / 文件开头写 `"""..."""` | 说明用途、参数、返回值，能被 `help()` 和 `__doc__` 读到 |

### ① 单行注释

```python
# 跳过表头行，第一行是列名不是数据
next(f)
```

### ② 行内注释（少用）

```python
age = 18   # 单位：岁
```

### ③ 多行注释：要写的说明超过一行，就用它

```python
"""
这段代码处理用户上传的文件：
1. 先用 strip() 去掉首尾空白，避免用户手抖多敲了空格
2. 再统一转小写，因为用户名比较时区分大小写
3. 最后查重，重复的用户名直接拒绝
"""
username = raw_input.strip().lower()
```

> ❌ 别这么写（每行一个 `#`，改起来要一行行加删）：
> ```python
> # 这段代码处理用户上传的文件
> # 先去空白，再转小写
> # 最后查重
> ```
> ✅ 写成上面的三引号多行注释，整块挪动、整块删除都方便。

### ④ 文档字符串 docstring（写在函数/类开头）

```python
def greet(username):
    """向指定用户问好。

    参数:
        username: 用户名，字符串
    返回:
        拼接好的问候语
    """
    return f"Hello, {username}!"

print(greet.__doc__)     # 能读到上面那段说明
help(greet)              # 交互式里 help() 展示的就是它
```

### 好注释 vs 坏注释

```python
# ❌ 废话注释
i = i + 1     # 把 i 加 1

# ✅ 有效注释
# 跳过表头行，第一行是列名不是数据
next(f)
```

**原则**：代码写完先想能不能靠好命名自解释，解释不了再写注释。

## 2 番外篇：数据类型

### 四大数据类型一图流

| 类型 | 英文名 | 例子 | 可变？ |
|------|--------|------|--------|
| 字符串 | `str` | `"hello"` | ❌ 不可变 |
| 整数 | `int` | `42` | ❌ |
| 浮点数 | `float` | `3.14` | ❌ |
| 布尔 | `bool` | `True` / `False` | ❌ |
| 列表 | `list` | `[1, 2, 3]` | ✅ 可变 |
| 字典 | `dict` | `{"a": 1}` | ✅ 可变 |
| 元组 | `tuple` | `(1, 2)` | ❌ 不可变 |
| 空值 | `NoneType` | `None` | — |

```python
type(42)          # <class 'int'>
type("42")        # <class 'str'>
type(42.0)        # <class 'float'>
isinstance(42, int)   # True
```

### 类型转换

```python
int("42")      # 42
int(3.9)       # 3   直接截断，不是四舍五入
float("3.14")  # 3.14
str(42)        # "42"
bool(0)        # False
bool("")       # False
bool("False")  # True ← 非空字符串都是 True！坑
```

### 不可变 vs 可变（理解这个能少踩一半坑）

```python
# 不可变：str
s = "python"
s.upper()          # 返回 'PYTHON'，但 s 没变
print(s)           # python
s = s.upper()      # 要回写才变

# 可变：list
nums = [1, 2, 3]
nums.append(4)     # 原地修改
print(nums)        # [1, 2, 3, 4]
```

### Python 之禅

```python
import this
```

> `Simple is better than complex.` —— 看不懂随时回来敲一遍。

## 动手练

1. 用变量存你的名字，用 `f-string` 打印一句自我介绍。
2. 输入 `>>> 0.1 + 0.2` 看结果，解释为什么会这样。
3. 把 `"  PYTHON  "` 处理成 `"Python"`（提示：`strip()` + `title()` 链式调用）。
4. 用 `removeprefix()` 把 `"https://www.bilibili.com"` 变成 `"www.bilibili.com"`。
