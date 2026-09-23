# 9 类

> 包含视频：`9 先导篇：搞懂面向对象编程`（08:45）、`9.1 创建和使用类`（03:54）、`9.2 使用类和实例`（09:31）、`9.3 继承`（07:22）

## 9 先导篇：搞懂面向对象编程（OOP）

### 面向过程 vs 面向对象

| | 面向过程 | 面向对象 |
|---|---------|---------|
| 核心 | 步骤/函数 | 对象（数据 + 行为） |
| 写法 | `make_pizza(size, toppings)` | `pizza.bake()` |
| 适合 | 简单脚本 | 复杂、需要复用和扩展的程序 |

**一句话理解**：
- **类（class）** = 图纸/模板，定义"这类东西有什么属性、能做什么"
- **对象/实例（instance）** = 按图纸造出来的具体东西

```
类 Dog（图纸）
 ├── 属性：name、age          ← 数据
 └── 方法：sit()、roll_over()  ← 行为
        ↓ 实例化
实例 my_dog = Dog('Willie', 6)   ← 一条具体的狗
```

### 为什么要用类

1. **封装**：把数据和操作数据的函数打包在一起
2. **复用**：一个类可以造无数个对象
3. **扩展**：继承让你可以基于已有的类改出新的类
4. **贴近现实**：现实世界就是由"对象"组成的，用类建模更自然

> 在《外星人入侵》项目里：飞船、子弹、外星人、按钮、计分板，每一个都是类。

## 9.1 创建和使用类

```python
class Dog:
    """一次模拟小狗的简单尝试。"""

    def __init__(self, name, age):
        """初始化属性 name 和 age。"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下。"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name} rolled over!")
```

### 关键概念逐个拆

| 概念 | 说明 |
|------|------|
| `class Dog:` | 定义一个类，类名用**驼峰命名**（每个单词首字母大写，无下划线） |
| `__init__()` | **构造方法**，创建实例时自动调用，首尾各两个下划线 |
| `self` | 指向**实例本身**的引用，必须是第一个参数（调用时不用传，Python 自动传） |
| `self.name` | **实例属性**，每个实例各有一份 |
| 类里的函数 | 叫**方法**，第一个参数必须是 `self` |

### 创建实例并访问

```python
my_dog = Dog('Willie', 6)            # 实例化，自动调用 __init__

print(f"My dog's name is {my_dog.name}.")      # 访问属性
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()                          # 调用方法（不用传 self）
my_dog.roll_over()
```

### 创建多个实例

```python
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)             # 两个实例互不影响

print(f"My dog is {my_dog.name}.")
print(f"Your dog is {your_dog.name}.")
my_dog.sit()
your_dog.sit()
```

## 9.2 使用类和实例

### 给属性指定默认值

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0          # 默认值，不必通过形参传入

    def get_descriptive_name(self):
        """返回整洁的描述性名称。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值。"""
        if mileage >= self.odometer_reading:          # 禁止回调里程表
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

### 修改属性的三种方式

```python
# ① 直接改（最简单，但没人拦得住你写脏数据）
my_new_car.odometer_reading = 23

# ② 通过方法改（推荐：可以在方法里加校验逻辑）
my_new_car.update_odometer(23)

# ③ 通过方法递增
my_used_car = Car('subaru', 'outback', 2019)
my_used_car.update_odometer(23_500)
my_used_car.increment_odometer(100)
```

> 原则：**能用方法就别直接改属性**，方法里可以加校验，直接改属性等于裸奔。

### 私有属性约定

```python
class BankAccount:
    def __init__(self):
        self._balance = 0        # 单下划线：约定「内部用，别外部访问」
        self.__secret = 1        # 双下划线：名称修饰（name mangling），更难误改
```

Python 没有真正的 private，靠约定。

## 9.3 继承

一个类**继承**另一个类时，自动获得父类的全部属性和方法，同时可以定义自己的。

- **父类（superclass）**：被继承的类
- **子类（subclass）**：继承者

```python
class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas_tank(self):
        """汽车有油箱。"""
        print("This car has a gas tank.")


class ElectricCar(Car):                 # ← 括号里写父类名
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)     # ← 调用父类的 __init__
        self.battery_size = 40                  # 子类特有的属性

    def describe_battery(self):                 # 子类特有的方法
        """打印一条描述电池容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):                    # 重写父类方法
        """电动汽车没有油箱。"""
        print("This car doesn't need a gas tank!")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())      # 继承自父类
my_leaf.describe_battery()                  # 子类自己的
my_leaf.fill_gas_tank()                     # 重写后调用的是子类版本
```

### `super()` 的作用

- 调用父类的方法（最常用于 `__init__`）
- **好处**：父类改了，子类不用跟着改；而且避免了重复代码

### 重写（override）

子类定义与父类**同名的方法**，就会覆盖父类版本。Python 只关心子类里有没有这个名字。

### 把实例用作属性（组合）

当某个部分的细节越来越多时，把它拆成一个独立类：

```python
class Battery:
    """一次模拟电动汽车电池的简单尝试。"""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        print(f"This car can go about {range_miles} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        # ← 实例作为属性
```

> **什么时候拆**：一个类的某个属性需要自己的属性和方法时，就该拆成小类。

## 9.4 导入类

```python
from car import Car                       # 导入单个类
from car import Car, ElectricCar          # 导入多个类
import car                                # 导入整个模块：car.Car()
from car import *                         # ❌ 不推荐
from electric_car import ElectricCar as EC   # 起别名
```

> 建议：一个模块放**一组相关**的类（比如 `car.py` 里放 `Car`、`Battery`、`ElectricCar`）。

## 9.5 类编码风格

- 类名用**驼峰命名法**：`ElectricCar`、`Battery`（不用下划线）
- 实例名、模块名用**小写 + 下划线**：`my_car`、`electric_car`
- 每个类下面写 docstring，简要描述功能
- 用空行组织：类内方法之间空一行，模块内类之间空两行
- 先写 `import` 标准库，空一行，再写自己的模块

## ⚠️ 常见坑

| 现象 | 原因 |
|------|------|
| `TypeError: __init__() missing 1 required positional argument: 'self'` | 调用的是**类**而不是实例，忘了加括号：`Dog.sit()` 应为 `Dog('a',1).sit()` |
| `AttributeError: 'X' object has no attribute 'y'` | 属性拼错，或在 `__init__` 里没定义 |
| 忘记写 `self` | 方法定义时漏了 `self` 参数 |
| 子类忘了 `super().__init__()` | 父类属性没有初始化，访问时 AttributeError |
| 类属性 vs 实例属性混淆 | 写在 `class` 下、方法外的属性是**所有实例共享**的 |

```python
class Dog:
    species = "Canis"      # 类属性：所有实例共享

    def __init__(self, name):
        self.name = name   # 实例属性：每个狗各有一份
```

## 动手练

1. 写一个 `Restaurant` 类：属性 `restaurant_name`、`cuisine_type`，方法 `describe_restaurant()`、`open_restaurant()`。创建 3 个实例。
2. 写 `User` 类：属性 `first_name`、`last_name`、`login_attempts`（默认 0），方法 `describe_user()`、`greet_user()`、`increment_login_attempts()`、`reset_login_attempts()`。
3. 继承练习：`IceCreamStand(Restaurant)`，加属性 `flavors`（列表）和方法 `show_flavors()`。
4. 组合练习：写 `Battery` 类作为 `ElectricCar` 的属性，加 `upgrade_battery()` 方法把容量提到 65。
