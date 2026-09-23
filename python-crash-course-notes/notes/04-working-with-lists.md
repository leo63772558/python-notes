# 4 操作列表

> 包含视频：`4.1 遍历整个列表`（04:07）、`4.3 创建数值列表`（04:53）

## 4.1 遍历整个列表

`for` 循环把列表里的元素挨个取出来，**对每个元素执行相同的操作**。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
```

### 语法三要素（缺一不可）

```
for 变量名 in 列表名:
    ↑              ↑
  临时变量       可迭代对象
                          ↑ 冒号
        ↑ 缩进（4 个空格）
```

- **冒号 `:`** 结尾
- **缩进**决定"哪些代码在循环里"，缩进错了逻辑就错了
- 循环结束后，执行缩进外的代码（这个缩进外的 `print` 只跑一次）

### 临时变量命名

```python
for cat in cats:
for dog in dogs:
for item in list_of_items:      # 单复数配对，可读性最好
```

### 循环里"忘记缩进"的四种后果

```python
magicians = ['alice', 'david', 'carolina']

# 1. 忘记缩进 → IndentationError
for m in magicians:
print(m)

# 2. 忘记冒号 → SyntaxError
for m in magicians
    print(m)

# 3. 不必要的缩进（循环外代码被缩进）→ 逻辑错误，不报错但结果错
message = "hi"
    print(message)              # IndentationError: unexpected indent

# 4. 循环后忘记缩进 → 本该每次执行的只执行最后一次
for m in magicians:
    msg = f"{m} nice"
print(msg)                      # 只打印最后一个人
```

## 4.2 `range()`：生成一串数

**完整格式：`range(起始点, 终止点, 步长)`**

```
range(start, stop, step)
        ↑        ↑       ↑
     起始点    终止点    步长 ← 写在最后一个位置，可省略，默认 1
   （可省略，     ↑
    默认 0）  取不到！左闭右开
```

三个位置的含义：

| 位置 | 名字 | 说明 |
|------|------|------|
| 第 1 个 | **起始点 start** | **包含**它；省略不写就是 `0` |
| 第 2 个 | **终止点 stop** | **取不到**！到 `stop - 1` 就停 —— 这叫**左闭右开** `[start, stop)` |
| 第 3 个 | **步长 step** | 每次加多少；默认 `1`；写**负数**就倒着走 |

```python
for x in range(1, 5):        # 起始 1，终止 5（取不到），步长默认 1
    print(x)                 # 1 2 3 4

for x in range(0, 10, 2):    # 步长写在最后一位
    print(x)                 # 0 2 4 6 8

for x in range(5, 0, -1):    # 负步长倒着走，注意起始点要比终止点大
    print(x)                 # 5 4 3 2 1

list(range(3))               # [0, 1, 2]  只写一个参数 = 只给了终止点，起始点默认 0
```

| 写法 | 结果 |
|------|------|
| `range(5)` | `0,1,2,3,4`（起始点省略，从 0 开始） |
| `range(1, 5)` | `1,2,3,4` |
| `range(1, 10, 2)` | `1,3,5,7,9`（步长 2） |
| `range(5, 0, -1)` | `5,4,3,2,1`（负步长，倒着走） |

> ⚠️ 新手第一大坑：**想打印 1～10 要写 `range(1, 11)`**，写 `range(1, 10)` 永远打不出 10。
> 记住"左闭右开"：**包左不包右**。

## 4.3 创建数值列表

### `list()` + `range()`

```python
numbers = list(range(1, 6))
print(numbers)          # [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))
print(even_numbers)     # [2, 4, 6, 8, 10]
```

### 经典案例：平方数

```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)          # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

更 Pythonic 的写法（第 3 版更推荐）：

```python
squares = [value ** 2 for value in range(1, 11)]
```

### 数值列表统计函数

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)      # 0
max(digits)      # 9
sum(digits)      # 45
len(digits)      # 10
sum(digits) / len(digits)   # 平均值
```

### 百万级数据不卡顿

```python
million = list(range(1, 1_000_001))
print(min(million), max(million), sum(million))
```

> Python 处理百万级列表毫无压力，这也是它适合做数据分析的原因。

## 4.4 切片：取列表的一部分

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])     # ['charles', 'martina', 'michael']   左闭右开
print(players[1:4])     # ['martina', 'michael', 'florence']
print(players[:4])      # 从头开始，0 可省
print(players[2:])      # 到末尾，最后一个索引可省
print(players[-3:])     # 最后三个
print(players[:])       # 复制整个列表
print(players[::2])     # 步长 2，隔一个取一个
print(players[::-1])    # 反转（得到新列表，原列表不变）
```

### 遍历切片

```python
for player in players[:3]:
    print(player.title())
```

### 复制列表（重点！）

```python
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]        # ✅ 真复制，两份独立
friend_foods.append('ice cream')

friend_foods = my_foods           # ❌ 同一个列表的两个名字，改一个两个都变
```

## 4.5 元组：不可变的列表

```python
dimensions = (200, 50)            # 圆括号
print(dimensions[0])              # 200  能读
dimensions[0] = 250               # ❌ TypeError: 'tuple' object does not support item assignment

for dimension in dimensions:      # 能遍历
    print(dimension)

dimensions = (400, 100)           # ✅ 整体重新赋值是可以的
```

> 单元素元组必须带逗号：`(3,)`，写 `(3)` 就是普通整数 3。

## 4.6 代码格式（PEP 8 要点）

- 缩进用 **4 个空格**，不用 Tab
- 每行不超过 **79 字符**，注释不超过 72
- 运算符两边加空格：`x = y + 1`
- 函数之间空两行，类内方法之间空一行
- PyCharm 里 `Ctrl + Alt + L`（macOS `⌘ + ⌥ + L`）一键格式化

## 动手练

1. 用 `for` 循环打印 `[1, 2, 3, 4, 5]` 每个数的平方。
2. 用 `range()` 打印 1～20，再用列表推导式生成 1～20 的立方列表。
3. 计算 1～1000 的和（一行代码：`sum(range(1, 1001))`），想想为什么比循环快。
4. 取 `[1..10]` 的前三个、后三个，以及用 `[::-1]` 反转。
