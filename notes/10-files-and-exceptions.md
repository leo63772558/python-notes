# 10 文件和异常

> 包含视频：`10 先导篇：文件路径`（03:02）、`10.1 读取文件`（05:46）、`10.2 写入文件`（05:17）、`10.3 异常`（07:45）

## 10 先导篇：文件路径

### 绝对路径 vs 相对路径

```text
/my_project/
├── main.py
└── data/
    └── pi_digits.txt
```

| 类型 | 写法 | 说明 |
|------|------|------|
| 相对路径 | `data/pi_digits.txt` | 相对于**当前工作目录**（运行程序的目录），推荐 |
| 绝对路径 | `/Users/eric/my_project/data/pi_digits.txt` | 从根目录写全，换台电脑就废了 |

```python
from pathlib import Path

path = Path('data/pi_digits.txt')       # 第 3 版推荐用 pathlib
print(path.name)        # pi_digits.txt
print(path.suffix)      # .txt
print(path.parent)      # data
print(path.exists())    # True / False
```

> ⚠️ Windows 路径用反斜杠 `\`，但在 Python 字符串里 `\` 是转义符。
> 解决方法：用 `pathlib`（自动处理）或用原始字符串 `r"C:\Users\..."`，或者统一写正斜杠 `/`。

## 10.1 读取文件

### 读取整个文件

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()          # 一次性读完，返回字符串
print(contents)
```

`read_text()` 会在末尾多留一个空行，用 `rstrip()` 去掉：

```python
contents = path.read_text().rstrip()
print(contents)
```

> 还可以指定编码：`path.read_text(encoding='utf-8')`，处理中文文件时很有用。

### 逐行读取

```python
from pathlib import Path

path = Path('pi_digits.txt')
for line in path.read_text().splitlines():
    print(line)
```

`splitlines()` 把字符串按行切成列表，每行不带换行符。

### 传统写法（第 2 版，了解即可）

```python
with open('pi_digits.txt') as f:
    contents = f.read()

with open('pi_digits.txt') as f:
    for line in f:
        print(line.rstrip())
```

> `with` 会在代码块结束后**自动关闭文件**，别直接用 `f = open(...)` 忘了 `close()`。

### 文件内容的使用

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()      # 去掉每行左边的空格

print(pi_string)
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

## 10.2 写入文件

### 写入空文件

```python
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.")      # 文件不存在就创建，存在就覆盖！
```

> ⚠️ `write_text()` 会**清空原内容**。要追加就用追加模式（见下）。

### 写入多行

```python
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
```

> ⚠️ `write_text()` **不会自动加换行**，多行必须自己写 `\n`。

### 追加到文件（传统写法）

```python
with open('programming.txt', 'a') as f:        # 'a' = append 追加模式
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I love creating apps that can run in a browser.\n")
```

文件打开模式速查：

| 模式 | 含义 |
|------|------|
| `'r'` | 读取（默认） |
| `'w'` | 写入（**清空**原内容） |
| `'a'` | 追加（末尾添加） |
| `'r+'` | 读写 |

## 10.3 异常

程序出错时 Python 会**抛出异常**。不处理 → 程序崩溃并显示 traceback。

### 常见异常类型

| 异常 | 触发场景 |
|------|---------|
| `ZeroDivisionError` | 除以 0 |
| `FileNotFoundError` | 打开不存在的文件 |
| `ValueError` | 类型转换失败，如 `int('abc')` |
| `TypeError` | 类型不匹配 |
| `IndexError` | 索引越界 |
| `KeyError` | 字典键不存在 |
| `AttributeError` | 访问不存在的属性 |

### `try-except` 基本结构

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### 完整结构：`try-except-else-finally`

```python
try:
    answer = int(a) / int(b)        # 可能出错的代码
except ZeroDivisionError:
    print("除数不能为 0")
except ValueError:
    print("请输入数字")
else:
    print(f"结果是 {answer}")        # 没出错才执行
finally:
    print("无论如何都会执行")         # 常用于关闭资源
```

### 处理 `FileNotFoundError`

```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # 统计文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
```

### 静默失败：`pass`

```python
def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass                    # 什么都不做，继续跑
    else:
        words = contents.split()
        print(f"{path} has about {len(words)} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(Path(filename))
```

> `pass` 也可以当占位符，表示"以后再写"。
> **静默失败要慎用**：出错时你什么都不知道，调试会很痛苦。至少打个日志。

### 主动抛出异常

```python
raise ValueError("参数必须是正数")
```

## 10.4 存储数据：`json`

`json` 模块让数据**持久化**（程序结束数据还在）。

### 保存 `json.dump()`

```python
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)      # 转成 JSON 字符串
path.write_text(contents)
```

或一步到位：

```python
path = Path('numbers.json')
path.write_text(json.dumps(numbers))
```

### 读取 `json.load()`

```python
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)      # [2, 3, 5, 7, 11, 13]
```

### 经典案例：记住用户名

```python
from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它。"""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None

def get_new_username(path):
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """问候用户，并指出其名字。"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

### JSON 能存什么

| Python | JSON |
|--------|------|
| dict | object |
| list / tuple | array |
| str | string |
| int / float | number |
| True / False | true / false |
| None | null |

> 自定义类的实例不能直接存 JSON，得先转成字典（`vars(obj)` 或写 `to_dict()` 方法）。

## 10.5 重构

**重构**：把能跑的代码拆成一系列函数，让结构更清晰、更易扩展。

原则：
1. 每个函数**只做一件事**
2. 函数名准确描述做什么
3. 先跑通，再重构，别同时做两件事

上面的 `greet_user()` 例子就是重构后的结果：把"读取"、"新建"、"问候"拆成三个函数。

## 动手练

1. 新建 `learning_python.txt`，写 3 行内容，用 `read_text()` 读出来打印；再逐行打印；再存到一个列表里在循环外打印。
2. 写程序询问用户名，写入 `guest.txt`；再写 `guest_book.txt`，每来一位访客追加一行记录。
3. 加法计算器：输入两个数字相加，用 `try-except` 处理 `ValueError`（输入了非数字）。
4. 猫和狗：读 `cats.txt` 和 `dogs.txt` 并打印，文件不存在时静默失败（用 `pass`）。
5. 记住你喜欢的数字：用 `json` 存一个数字，下次运行直接读出来告诉你。
