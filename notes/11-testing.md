# 11 测试代码

> 包含视频：`11.1 测试函数`（05:01）、`11.2 测试类`（08:09）
> ⚠️ 第 3 版重大变化：本章从 `unittest` 改为 **`pytest`**（行业标准）

## 为什么要写测试

- 改代码后能立刻知道**有没有改坏**
- 测试是"代码的说明书"，别人看测试就知道你的函数怎么用
- 专业 Python 岗位必备技能

## 安装 pytest

```bash
pip install pytest
pytest --version
```

> 如果报 `command not found`，用 `python -m pytest`。

## 11.1 测试函数

### 被测代码（`name_function.py`）

```python
def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名。"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

### 测试文件（`test_name_function.py`）

**命名规则：测试文件必须以 `test_` 开头，测试函数也必须以 `test_` 开头。**

```python
from name_function import get_formatted_name

def test_first_last_name():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
```

### 运行

```bash
pytest
```

输出解读：

```
========================= test session starts ==========================
collected 2 items

test_name_function.py ..                                      [100%]

========================== 2 passed in 0.03s ==========================
```

| 符号 | 含义 |
|------|------|
| `.` | 通过（passed） |
| `F` | 失败（failed） |
| `E` | 出错（error） |

常用命令：

```bash
pytest                          # 跑当前目录所有测试
pytest test_name_function.py    # 只跑某个文件
pytest -v                       # 详细模式，显示每个测试名
pytest -k "middle"              # 只跑名字含 middle 的测试
pytest -x                       # 第一次失败就停
```

### `assert` 断言

```python
assert 条件                    # 条件为假 → AssertionError，测试失败
assert 条件, "失败时的提示信息"
```

常用断言：

```python
assert a == b
assert a != b
assert a in b
assert a is True
assert value > 0
```

### 测试失败的诊断流程

1. 看是哪个测试失败（`FAILED test_xxx.py::test_yyy`）
2. 看 `assert` 那行的实际值 vs 期望值
3. **先怀疑测试写错了，再怀疑代码错了**（真的，很多时候是测试写错）
4. 改代码，不要改测试去迁就错误的逻辑

### 修复示例

假设发现 `get_formatted_name` 处理中间名有 bug，改完代码后**再跑一次 pytest**，确认测试通过 —— 这就是测试的价值。

## 11.2 测试类

### 被测类（`survey.py`）

```python
class AnonymousSurvey:
    """收集匿名调查问卷的答案。"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备。"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷。"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷。"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷。"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

### 用 fixture 复用测试对象

`fixture` 是 pytest 的核心机制：把"准备测试对象"的代码抽出来，多个测试共用。

```python
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的 AnonymousSurvey 实例。"""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)

def test_store_single_response(language_survey):
    """测试单个答案会被妥善地存储。"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """测试三个答案会被妥善地存储。"""
    for response in ['English', 'Spanish', 'Mandarin']:
        language_survey.store_response(response)
    for response in ['English', 'Spanish', 'Mandarin']:
        assert response in language_survey.responses
```

用法：把 fixture **函数名**作为参数传给测试函数，pytest 会自动调用它并注入返回值。

> 好处：每个测试函数拿到的都是**全新的**实例，测试之间互不干扰。

### 一个更完整的类测试例子

```python
# employee.py
class Employee:
    """收集员工信息的简单尝试。"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """默认加薪 5000，也可以指定其他金额。"""
        self.annual_salary += amount
```

```python
# test_employee.py
import pytest
from employee import Employee

@pytest.fixture
def employee():
    return Employee('eric', 'matthes', 100_000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 105_000

def test_give_custom_raise(employee):
    employee.give_raise(10_000)
    assert employee.annual_salary == 110_000
```

## pytest 常用技巧

### 参数化：一次测多组数据

```python
import pytest
from name_function import get_formatted_name

@pytest.mark.parametrize("first,last,expected", [
    ('janis', 'joplin', 'Janis Joplin'),
    ('wolfgang', 'mozart', 'Wolfgang Mozart'),
    ('mary', 'jane', 'Mary Jane'),
])
def test_names(first, last, expected):
    assert get_formatted_name(first, last) == expected
```

### 测试异常

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

### 临时目录（测文件读写很好用）

```python
def test_write_file(tmp_path):
    p = tmp_path / "test.txt"
    p.write_text("hello")
    assert p.read_text() == "hello"
```

`tmp_path` 是 pytest 内置 fixture，自动给你一个干净的临时目录。

### 跳过 / 标记预期失败

```python
@pytest.mark.skip(reason="功能还没实现")
def test_not_ready():
    ...
```

## 测试文件组织建议

```
project/
├── name_function.py
├── survey.py
├── tests/
│   ├── __init__.py
│   ├── test_name_function.py
│   └── test_survey.py
└── pytest.ini          # 可选：配置 pytest 行为
```

`pytest.ini` 示例：

```ini
[pytest]
testpaths = tests
python_files = test_*.py
```

## ✅ 测试编写清单

- [ ] 文件名 `test_xxx.py`，函数名 `test_xxx`
- [ ] 一个测试只测**一个行为**
- [ ] 覆盖三种情况：正常输入、**边界值**、异常输入
- [ ] 用 fixture 消除重复代码
- [ ] 测试之间互相独立，不依赖执行顺序
- [ ] 改完代码跑一遍 pytest

## 动手练

1. 给 `get_formatted_name()` 加测试用例，覆盖「只有名和姓」「带中间名」两种情况，跑 pytest 看结果。
2. 写 `Employee` 类和上面三个测试（默认加薪、自定义加薪、不改原值）。
3. 给第 8 章的 `make_album()` 写测试，验证返回的字典键是否正确。
4. 写一个会失败的测试，观察 `pytest -v` 的输出长什么样（学会看报错很重要）。
