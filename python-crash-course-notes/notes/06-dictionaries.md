# 6 字典

> 包含视频：`6.2 使用字典`（06:07）、`6.3 遍历字典`（04:33）、`6 番外篇：格式化字符串`（03:20）

## 6.1 一个简单的字典

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])     # green
print(alien_0['points'])    # 5
```

字典 = **键值对（key-value）集合**，用 `{}` 表示。

```
{'color': 'green', 'points': 5}
   ↑         ↑
  key      value
```

## 6.2 使用字典

### 访问值

```python
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
```

> ⚠️ 键不存在 → `KeyError: 'xxx'`
> 安全访问用 `get()`：

```python
alien_0.get('speed', 'No speed value assigned.')   # 不存在时返回默认值，不报错
```

### 添加键值对

```python
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0          # 直接赋值，键存在就改，不存在就加
alien_0['y_position'] = 25
print(alien_0)
```

### 从空字典开始

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
```

### 修改值

```python
alien_0['color'] = 'yellow'
```

### 删除键值对 `del`

```python
del alien_0['points']        # 永久删除，KeyError 风险同上
```

### 一个对象的多个同类信息：字典 vs 列表

```python
# 多个外星人：列表套字典
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens: {len(aliens)}")
```

### 由类似对象组成的字典（一个键对应多个值）

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 值也可以是列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
}
```

> 格式建议：键值较长时，左花括号后换行，每个键值对缩进 4 空格，**末尾保留一个逗号**（方便后续追加）。

## 6.3 遍历字典

三种遍历方式，必须分清：

```python
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

# ① 遍历所有键值对 .items()
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# ② 只遍历键 .keys()
for name in user_0.keys():
    print(name.title())
# 只写 for name in user_0: 效果一样（默认就是遍历键）
# 但显式写 .keys() 可读性更好

# ③ 只遍历值 .values()
for value in user_0.values():
    print(value)
```

### 遍历键时的经典用法：判断某人是否在字典里

```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
```

### 按顺序遍历

```python
for name in sorted(favorite_languages.keys()):     # 按字母升序
    print(f"{name.title()}, thank you for taking the poll.")
```

### 去重：遍历值用 `set()`

```python
for language in set(favorite_languages.values()):   # 去掉重复的 'python'
    print(language.title())
```

> 集合 `set`：无序、元素唯一。可用 `{}` 直接创建：`{'python', 'c'}`，空集合必须用 `set()`。

## 6.4 嵌套

### ① 列表里放字典

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
```

### ② 字典里放列表

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
    print(f"\tAdding {topping}.")
```

### ③ 字典里放字典

```python
users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
    'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris'},
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

> ⚠️ 嵌套别超过 2～3 层，太深就该考虑用**类**（第 9 章）了。

## 6 番外篇：格式化字符串

### f-string 完整语法

```python
name = "Eric"
age = 46

# 基本插值
print(f"Hello, {name}. You are {age}.")

# 表达式
print(f"{2 + 3}")                       # 5
print(f"{age >= 18}")                   # True

# 数字格式化
price = 1234.5678
print(f"{price:.2f}")                   # 1234.57   保留 2 位小数
print(f"{price:,.2f}")                  # 1,234.57  千分位
print(f"{0.25:.1%}")                    # 25.0%     百分比
print(f"{1234567:e}")                   # 1.234567e+06  科学计数法

# 宽度与对齐
print(f"|{'hello':>10}|")               # |     hello|   右对齐
print(f"|{'hello':<10}|")               # |hello     |   左对齐
print(f"|{'hello':^10}|")               # |  hello   |   居中
print(f"{7:03d}")                       # 007  补零

# 字典取值
print(f"{user_0['username']}")
# ⚠️ 注意引号嵌套：f 字符串用双引号，里面就用单引号
```

### 对比老写法（了解即可，别用）

```python
"Hello, {}. You are {}.".format(name, age)     # str.format()
"Hello, %s. You are %d." % (name, age)         # % 格式化
```

### 转义花括号

```python
print(f"{{literal braces}}")     # {literal braces}
```

## 字典常用操作速查

| 操作 | 写法 |
|------|------|
| 访问 | `d['k']` / `d.get('k', default)` |
| 添加/修改 | `d['k'] = v` |
| 批量更新 | `d.update({'a': 1})` |
| 删除 | `del d['k']` / `d.pop('k')` |
| 删除并返回 | `d.popitem()`（删最后一对） |
| 判断键存在 | `'k' in d` |
| 键数 | `len(d)` |
| 设置默认值 | `d.setdefault('k', v)` |

## 动手练

1. 建一个自己的信息字典（姓名/年龄/城市），用 `for k, v in d.items()` 打印。
2. 用列表套字典管理 3 个宠物，遍历打印每只的类型和主人名。
3. 调查 5 位朋友喜欢的编程语言，用 `set()` 统计一共有哪几种语言。
4. 用 f-string 把 `3.14159` 格式化成 `3.14`、`3.1416`、`0003.14` 三种样子。
