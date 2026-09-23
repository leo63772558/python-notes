# 5 if 语句

> 包含视频：`5.2–5.3 条件测试与 if 语句`（02:35）、`5.3 更多 if 语句`（06:12）、`5 番外篇：逻辑运算`（02:57）

## 5.1 一个简单示例

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

## 5.2 条件测试

条件测试的核心：一个**求值为 `True` 或 `False` 的表达式**。

### 比较运算符

| 符号 | 含义 | 例子 |
|------|------|------|
| `==` | 等于 | `1 == 1` → True |
| `!=` | 不等于 | `1 != 2` → True |
| `<` `>` | 小于/大于 | `2 < 3` → True |
| `<=` `>=` | 小于等于/大于等于 | `3 >= 3` → True |
| `and` | 与（都真才真） | `1 < 2 and 2 < 3` |
| `or` | 或（一个真就真） | `1 > 2 or 2 < 3` |
| `not` | 非（取反） | `not True` → False |

```python
age = 19
age == 19        # True
age < 21         # True
age <= 21 and age >= 18    # True   （也可以写 18 <= age <= 21）
```

> ⚠️ **`=` 是赋值，`==` 是比较**。写 `if age = 19:` 直接 `SyntaxError`。
> ⚠️ 字符串比较**区分大小写**：`'Audi' == 'audi'` 是 False。
> 需要忽略大小写就先统一：`car.lower() == 'audi'`。

### 检查是否包含 / 不包含

```python
banned_users = ['andrew', 'carolina', 'david']
'bob' in banned_users            # False
'bob' not in banned_users        # True

# 结合 if
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response.")
```

### 布尔表达式

```python
game_active = True
can_edit = False
```

命名习惯：布尔变量用 `is_xxx` / `has_xxx` / `can_xxx`，比如 `is_running`。

## 5.3 if 语句的四种结构

### ① 单分支 `if`

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

### ② 双分支 `if-else`

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
```

### ③ 多分支 `if-elif-else`

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
```

- `elif` 可以写任意多个
- **`else` 可以省略**：省略后逻辑更清晰（不满足就什么都不做）

```python
# 推荐：省略 else，条件更明确
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
```

- ⚠️ `if-elif` 链是**短路的**：一旦某个条件成立，后面的都不再判断。

### ④ 多个独立的 `if`（不是 elif）

当你想检查**多个互不排斥**的条件时：

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
```

> **if-elif vs 多个 if**：
> - 只跑其中一个分支 → `if-elif-else`
> - 每个条件都要检查 → 多个独立 `if`

## 5.4 用 if 处理列表

### 检查特殊元素

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
```

### 判断列表是否为空（重要！）

```python
requested_toppings = []

if requested_toppings:              # ✅ 非空列表为 True，空列表为 False
    for t in requested_toppings:
        print(f"Adding {t}.")
    print("\nFinished!")
else:
    print("Are you sure you want a plain pizza?")
```

### 同时使用多个列表

```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
```

## 5 番外篇：逻辑运算

### 真值表

| `a` | `b` | `a and b` | `a or b` | `not a` |
|-----|-----|-----------|----------|---------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

### 除了 `and` `or` `not`：还有 `&` `|` `!` 吗？

先给对照表：

| 你想要 | Python 正确写法 | 别的语言常见写法（Python 里**不是**这么写） |
|--------|----------------|------------------------------------------|
| 与（都真才真） | `and` | `&&`、`&` |
| 或（一个真就真） | `or` | `\|\|`、`\|` |
| 非（取反） | `not` | `!`、`~` |

**`&` `|` `^` `~` 在 Python 里是「位运算符」**（按二进制位算），不是逻辑运算符：

```python
5 & 3      # 1    101 & 011 = 001（按位与）
5 | 3      # 7    101 | 011 = 111（按位或）
5 ^ 3      # 6    异或：不同为 1
~5         # -6   按位取反

True & False      # False —— 碰巧结果一样，但这不是逻辑运算
True | False      # True
```

#### 三个必须记住的坑

1. **`!` 在 Python 里根本不是运算符。** 取反写 `not`，"不等于"写 `!=`。写 `if !x:` 直接 `SyntaxError`。
2. **`&` / `|` 不短路**，两边都会执行，容易炸：

```python
False & (1 / 0)     # ❌ ZeroDivisionError：右边照算不误
False and (1 / 0)   # ✅ False：and 短路，右边根本不看
```

3. **优先级不一样**：`&` `|` 比比较运算符优先级**高**，会把代码算歪：

```python
1 & 2 == 2      # 实际算成 (1 & 2) == 2 → False，不是你想要的 1 & (2 == 2)
age >= 18 & age < 65    # ❌ 会被算成 age >= (18 & age) < 65，结果完全不对
```

#### 结论

> **if 里做条件判断，一律用 `and` / `or` / `not`；**
> `&` `|` `^` `~` 只在做二进制运算时才用；
> 唯一例外是**集合**：`set_a & set_b`（交集）、`set_a | set_b`（并集）是正规用法。

```python
if age >= 18 and age < 65:      # ✅
if not is_closed:               # ✅ 取反
if x != 0:                      # ✅ 不等于，没有 ! 这种写法
if age >= 18 & age < 65:        # ❌ 永远别这么写
```

### 短路求值（面试常问）

```python
# and：左边为 False，右边就不执行了
False and print("不会执行")

# or：左边为 True，右边就不执行了
True or print("不会执行")

# 实用技巧：用短路避免报错
lst = []
if lst and lst[0] == 1:      # 先判空，避免 IndexError
    ...

# or 给默认值
name = input("name: ") or "anonymous"
```

### 优先级：`not` > `and` > `or`

```python
True or False and False    # → True（先算 and）
# 等价于 True or (False and False)
```

**别背优先级，加括号**：`(a or b) and c`

### Python 里的"假值"（记住这 6 个）

```python
bool(0)        # False
bool(0.0)      # False
bool("")       # False
bool([])       # False
bool({})       # False
bool(None)     # False
# 其他一切都是 True（包括 "False"、"0"、[0]）
```

## 代码风格

```python
# ✅ 推荐：简单条件
if age >= 18:
# ❌ 不推荐：多余的括号
if (age >= 18):

# 比较运算符两侧留空格
if x < 10 and y > 5:
```

## 动手练

1. 写程序：输入年龄，打印「儿童/青少年/成年/老年」四个阶段票价。
2. 判断用户名是否是 `'admin'`，是则打印特殊问候语，否则打印普通问候；列表为空时提示"需要找用户"。
3. 检查 5 以内的数和 5 以上的数，用 `if-elif-else` 打印不同提示。
4. 用 `in` 判断 `'python'` 是否在给定列表中。
