# 3 列表简介

> 包含视频：`3.1–3.3 列表及列表操作`（09:06）

## 3.1 列表是什么

列表 = **有序的可变容器**，用 `[]` 表示，元素之间逗号分隔。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)          # ['trek', 'cannondale', 'redline', 'specialized']
```

列表里可以放**任意类型**，也能混着放：

```python
mixed = [1, "two", 3.0, True, [4, 5]]
```

### 访问元素（索引从 0 开始）

```python
print(bicycles[0])       # trek
print(bicycles[-1])      # specialized   ← 负数索引：倒数第一个
print(bicycles[-2])      # redline
print(f"我的第一辆车是 {bicycles[0].title()}。")
```

> ⚠️ 索引越界 → `IndexError: list index out of range`。
> 取最后一个元素**优先用 `-1`**，不用 `len(list) - 1`。

## 3.2 修改、添加和删除元素

### 改：直接按索引赋值

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)       # ['ducati', 'yamaha', 'suzuki']
```

### 增：三种方式

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')        # 末尾追加（最常用）
motorcycles.insert(0, 'kawasaki')   # 指定位置插入，原元素右移
motorcycles.extend(['a', 'b'])      # 批量追加另一个列表

# 从空列表开始搭
nums = []
nums.append(1)
nums.append(2)
```

### 删：三种方式，区别必须分清

| 方式 | 语法 | 返回值 | 用在哪 |
|------|------|--------|--------|
| `del` | `del list[0]` | 无 | 知道索引，且不再需要这个值 |
| `pop()` | `list.pop()` / `list.pop(i)` | **返回被删的值** | 删了还要用（最常见） |
| `remove()` | `list.remove('honda')` | 无 | 只知道值，不知道索引 |

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

# del：按索引删，删了就没了
del motorcycles[0]

# pop：弹出，能接住
last_owned = motorcycles.pop()          # 默认弹最后一个
print(f"我最后拥有的是 {last_owned.title()}。")
first_owned = motorcycles.pop(0)        # 指定索引

# remove：按值删，只删第一个匹配项
motorcycles.remove('ducati')            # 值不存在 → ValueError
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
```

> ⚠️ `remove()` 只删**第一个**匹配值，要删光所有重复项得用循环或列表推导式。
> ⚠️ 别用 `list.remove()` 当 `del` 用：`remove` 是找值，`del`/`pop` 是找位置。

### 清空

```python
motorcycles.clear()      # 变成 []
```

## 3.3 组织列表

### 永久排序 `sort()`

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                   # 按字母升序，原地修改，无返回值
print(cars)                   # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)       # 降序
```

### 临时排序 `sorted()`

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))           # 返回新列表，原列表不变
print(cars)                   # 还是原顺序
```

> 反向遍历技巧：`for car in sorted(cars, reverse=True):`

### 倒着打印 `reverse()`

```python
cars.reverse()      # 原地反转（不是排序！只是倒序排列）
```

### 长度 `len()`

```python
len(cars)      # 4   ← 注意：从 1 开始数，索引从 0 开始，差 1 是经典 off-by-one 错误
```

### 其他高频操作

```python
nums = [2, 4, 2, 6, 2]
nums.count(2)        # 3     统计出现次数
nums.index(4)        # 1     返回第一次出现的索引，找不到 → ValueError
2 in nums            # True  成员判断（列表/字符串/字典都能用）
len(nums)            # 5
```

### 拼接与复制

```python
a = [1, 2]
b = [3, 4]
print(a + b)         # [1, 2, 3, 4]  生成新列表
a.extend(b)          # a 变成 [1, 2, 3, 4]  原地修改

# 复制：必须用 copy() 或切片，别用 =
c = a.copy()         # ✅ 独立副本
d = a[:]             # ✅ 切片复制，等价效果
e = a                # ❌ 只是起了个别名，改 e 就是改 a
```

## ⚠️ 索引陷阱速查

```python
lst = ['a', 'b', 'c']
lst[3]        # IndexError
lst[-4]       # IndexError
lst.pop(9)    # IndexError: pop index out of range
lst.remove('z')  # ValueError: list.remove(x): x not in list
```

**取索引前先确认长度**：

```python
if lst:                       # 空列表是 False，非空是 True
    print(lst[0])
```

## 动手练

1. 建一个 `friends` 列表，用 `append()` 加 3 个人，用 `f-string` 逐个打印邀请语。
2. 用 `pop()` 模拟"有朋友来不了"，更换嘉宾并重新发邀请。
3. 把 `[3, 1, 4, 1, 5]` 排序后打印，再用 `sorted()` 打印一次临时结果，观察原列表是否被改。
4. 打印 `len()`，然后**故意**访问 `list[len(list)]`，记住这个报错长什么样。
