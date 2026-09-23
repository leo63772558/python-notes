# 8 函数

> 包含视频：`8.1 定义函数`（05:28）、`8.3 返回值`（05:23）

## 8.1 定义函数

函数 = **给一段代码起名字**，需要时调用，不用重复粘贴。

```python
def greet_user():
    """显示简单的问候语。"""        # 文档字符串 docstring
    print("Hello!")

greet_user()                        # 调用
```

结构：

```python
def 函数名(参数):
    """文档字符串"""
    函数体
    return 返回值（可选）
```

### 向函数传递信息

```python
def greet_user(username):
    """显示问候语。"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

- **形参（parameter）**：函数定义里的变量，如 `username`
- **实参（argument）**：调用时实际传进去的值，如 `'jesse'`

## 8.2 传递实参

### ① 位置实参（按顺序对应）

```python
def describe_pet(animal_type, pet_name):
    """显示宠物信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

> ⚠️ 顺序错了结果就错（会把 hamster 当成名字），记不住顺序就用关键字实参。

### ② 关键字实参（`名=值`）

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')   # 顺序无所谓
```

### ③ 默认值

```python
def describe_pet(pet_name, animal_type='dog'):      # 有默认值的参数必须放后面
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')                     # 用默认值 dog
describe_pet('willie')                              # 位置实参也行
describe_pet('harry', 'hamster')                    # 覆盖默认值
```

> ⚠️ **定义时**：无默认值的参数在前，有默认值的在后，否则 `SyntaxError`。
> ⚠️ 默认值不要用可变对象（见"坑位"章节）。

### ④ 让实参变成可选的

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)              # Jimi Hendrix
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)              # John Lee Hooker
```

**技巧**：把可选参数的默认值设为空字符串，放在最后。

## 8.3 返回值

函数用 `return` 把结果交给调用者。

```python
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

### 返回字典/列表

```python
def build_person(first_name, last_name, age=None):
    """返回一个字典，包含一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:                          # age 为 None 时不加进字典
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)     # {'first': 'jimi', 'last': 'hendrix', 'age': 27}
```

### `return` 的几个细节

```python
def f():
    return 1
    print("这里永远执行不到")     # return 之后的代码不执行

def g():
    pass                          # 没有 return → 隐式返回 None

def h():
    return 1, 2, 3                # 返回元组 (1, 2, 3)
a, b, c = h()                     # 元组解包
```

### 结合 while 循环

```python
def get_formatted_name(first_name, last_name):
    return f"{first_name} {last_name}".title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

## 8.4 传递列表

```python
def greet_users(names):
    """向列表中的每位用户发出简单问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

### ⚠️ 在函数中修改列表（永久生效！）

```python
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止。"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# 运行后 unprinted_designs 变空了 —— 这是有意的，节省内存
```

### 禁止函数修改列表 → 传副本

```python
print_models(unprinted_designs[:], completed_models)
#            ↑ 切片副本，原列表保持不变
```

> 代价是复制一份，占用内存和时间。大列表慎用，小列表随意。

## 8.5 传递任意数量的实参

### `*args`：任意个位置实参（存成元组）

```python
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

### 结合位置实参使用

```python
def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

> `*toppings` 必须放在参数列表最后（它把剩下所有实参都收走）。

### `**kwargs`：任意个关键字实参（存成字典）

```python
def build_profile(first, last, **user_info):
    """创建一个字典，包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
# {'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```

## 8.6 将函数存储在模块中

**模块** = 独立的 `.py` 文件，能被 `import` 到其他程序里。好处：代码复用、主程序干净、可分享。

```python
# pizza.py
def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

```python
# making_pizzas.py
import pizza                       # 导入整个模块

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 四种导入方式

| 写法 | 用法 | 说明 |
|------|------|------|
| `import module` | `module.func()` | 最安全，不会重名 |
| `import module as m` | `m.func()` | 起别名：`import numpy as np` |
| `from module import func` | `func()` | 直接用，但可能覆盖同名函数 |
| `from module import func as f` | `f()` | 别名避免冲突 |
| `from module import *` | `func()` | ❌ 别用，容易重名且难排查 |

### 模块写法建议

- 函数名要有描述性，只用小写 + 下划线
- 每个函数都写 docstring
- 模块文件里不要在顶层写测试调用（会被 import 时执行）

## ⚠️ 坑位：可变默认参数

```python
# ❌ 错误示范：默认列表只在函数定义时创建一次，会一直累积
def add_item(item, target=[]):
    target.append(item)
    return target

add_item(1)     # [1]
add_item(2)     # [1, 2]  ← 惊不惊喜？

# ✅ 正确写法
def add_item(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

## 动手练

1. 写一个 `favorite_book(title)`，打印"One of my favorite books is XXX"。
2. 写 `describe_city(city, country='China')`，打印"Xxx is in Xxx"。
3. 写 `make_album(artist, title, songs=None)`，返回字典，用 while 循环让用户不断输入直到 `q`。
4. 写 `show_magicians(magicians)` 遍历打印，再写 `make_great(magicians)` 给每人加上 "the Great"，注意别改原列表。
5. 把上面的函数拆到 `functions.py` 里，`import` 进来调用。
