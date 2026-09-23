# 7 用户输入和 while 循环

> 包含视频：`7.1 函数 input() 的工作原理`（04:19）、`7.2 while 循环简介`（05:47）

## 7.1 函数 `input()` 的工作原理

`input()` 让程序**暂停**，等用户从键盘输入，回车后继续。

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

### ⚠️ 最重要的一点：`input()` 返回的永远是字符串

```python
age = input("How old are you? ")
print(age)              # "18"（字符串）
age >= 18               # ❌ TypeError: '>=' not supported between 'str' and 'int'

age = int(age)          # ✅ 转成整数
if age >= 18:
    print("You can vote.")
```

**用的时候立刻转换**：

```python
height = float(input("How tall are you, in inches? "))
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

### 求模运算符判奇偶

```python
number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

### 提示语写法

```python
# 短提示：直接写在括号里
name = input("Please enter your name: ")

# 长提示：先存变量，提示末尾加空格
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
```

## 7.2 while 循环简介

`for` 循环：遍历**已知长度**的集合。
`while` 循环：**条件为真就一直跑**，不知道要跑多少次。

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1      # ⚠️ 忘了这行就是死循环！
```

> 死循环了？`Ctrl + C` 强制中断。

### 让用户决定何时退出

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""                       # 先给个初值，否则 while 判断时 NameError
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### 用标志（flag）控制循环 —— 推荐写法

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True                      # 标志变量
while active:
    message = input(prompt)
    if message == 'quit':
        active = False             # 一个条件就能终止，多个退出条件时特别好使
    else:
        print(message)
```

> 复杂程序里优先用 flag：退出条件可以写在循环体任意位置，逻辑更清晰。

### `break`：立刻跳出整个循环

```python
while True:
    city = input("\nPlease enter the name of a city you have visited:")
    if city == 'quit':
        break                      # 不再执行循环里剩下的代码
    print(f"I'd love to go to {city.title()}!")
```

> `break` 对 `for` 循环同样有效。任何循环里都能用。

### `continue`：跳过本轮，回到循环开头

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue                   # 偶数不打印，直接进入下一轮
    print(current_number)          # 1 3 5 7 9
```

> ⚠️ `continue` 前必须更新计数变量，否则死循环（经典翻车点）。

### `while True:` 惯用法

```python
while True:
    # 做事
    if 满足退出条件:
        break
```

## 7.3 用 while 处理列表和字典

### 在列表之间移动元素

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:                      # 列表非空就继续
    current_user = unconfirmed_users.pop()    # 从末尾弹
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

### 删除列表中所有特定值的元素

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:        # remove() 一次只删一个，用 while 删干净
    pets.remove('cat')

print(pets)                 # ['dog', 'dog', 'goldfish', 'rabbit']
```

### 用用户输入填充字典

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```

## 💡 实用模式：输入校验模板

```python
while True:
    raw = input("请输入 1-100 的整数：").strip()
    if not raw.isdigit():
        print("必须是数字，请重试")
        continue
    num = int(raw)
    if not 1 <= num <= 100:
        print("超出范围，请重试")
        continue
    break
print(f"你输入的是 {num}")
```

字符串判断方法（校验输入很好用）：

```python
"123".isdigit()      # True   是否全是数字
"-3".isdigit()       # False  负数不算
"abc".isalpha()      # True   是否全是字母
"abc123".isalnum()   # True   字母或数字
"  ".isspace()       # True   是否全是空白
```

## 动手练

1. 三明治配料：循环询问配料，输入 `quit` 结束，并打印"已加入 XX"。
2. 电影票：循环询问年龄，按年龄段打印票价，直到输入 `quit`。
3. 熟食店卖光了 `pastrami`：用 `while 'pastrami' in list: remove()` 处理。
4. 梦想度假地调查：用字典收集名字 + 地点，最后汇总打印。
5. 写一个"猜数字"游戏：随机 1～100，用 `while True` 循环到猜中为止（提示：`import random`）。
