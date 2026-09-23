# 1 起步：搭建编程环境

> 包含视频：`1 先导篇：为什么安装 Python 和 PyCharm`（01:25）、`1.1–1.2 搭建编程环境（macOS）`（04:44）、`1.1–1.2 搭建编程环境（Windows）`（04:46）、`1 番外篇：创建 PyCharm 项目`（04:38）

## 1 先导篇：为什么要装 Python 和 PyCharm

- **Python** 是解释器：你写的 `.py` 文件靠它跑起来。没装它，代码就是一堆文本。
- **PyCharm** 是 IDE（集成开发环境）：写代码、补全、调试、管理项目。
  - 书里第 3 版推荐 **VS Code**，本套视频用 **PyCharm Community（免费版）**，两者都能跑，选一个跟到底即可。

一句话理解三者关系：

```
你（人） → PyCharm（写代码的本子） → Python（干活的引擎） → 终端（看结果）
```

## 1.1 安装 Python（macOS）

1. 打开 [python.org/downloads](https://www.python.org/downloads/) 下载 **3.11+** 安装包。
2. 一路点继续安装。
3. **装完必须再跑一次**安装包里的 `Install Certificates.command`（否则后面 `pip` 装库会报 SSL 错误）。
4. 验证：

```bash
python3 --version     # Python 3.11.x
python3               # 进入交互式解释器，出现 >>> 就成功
print("Hello Python world!")
exit()                # 退出
```

> macOS 自带的 `python` 可能是 2.7，**用 `python3`**，别用 `python`。

## 1.1 安装 Python（Windows）

1. 去 python.org 下载 Windows installer（64-bit）。
2. **务必勾选 `Add python.exe to PATH`** —— 这是 Windows 上 90% 新手报错的根源。
3. 选 `Install Now`，装完验证：

```powershell
python --version
python
>>> print("Hello Python world!")
>>> exit()
```

如果提示「不是内部或外部命令」，说明 PATH 没勾上：
重新运行安装包 → `Modify` → 勾上 `Add Python to environment variables`；或者卸载重装。

## 1.2 安装 PyCharm

- 下载 **PyCharm Community Edition**（社区版免费，够用）：jetbrains.com/pycharm/download
- Windows 安装时注意勾：
  - `Add "Open Folder as Project"`（右键文件夹直接开项目）
  - `Add launchers dir to the PATH`
- macOS：把 `PyCharm.app` 拖进 Applications。

## 1 番外篇：创建 PyCharm 项目

**正确流程（建议养成习惯，每个练习一个项目）：**

1. `New Project` → 位置填 `python_work`（专门放练习的文件夹）
2. 解释器选择：
   - `Previously configured interpreter` → 找到刚装的 Python 3.11
   - 或 `New Virtualenv environment`（推荐！每个项目独立环境，装库不打架）
3. `Create`
4. 右键项目 → `New` → `Python File` → 命名 `hello_world`
5. 写：

```python
print("Hello Python world!")
```

6. 运行：右键 → `Run 'hello_world'`，或快捷键
   - Windows：`Ctrl + Shift + F10`
   - macOS：`Control + Shift + R`

## 三种运行方式（都要会）

| 方式 | 场景 | 命令 |
|------|------|------|
| IDE 点 Run | 日常开发 | — |
| 终端跑单文件 | 部署/脚本 | `python hello_world.py` |
| 交互式 `>>>` | 验证一句语法 | `python` |

## ⚠️ 新手高频坑位

| 现象 | 原因 | 解决 |
|------|------|------|
| `'python' 不是内部或外部命令` | PATH 没勾 | 重装勾 PATH |
| macOS 里 `python` 是 2.7 | 系统自带老版本 | 用 `python3` |
| 终端能跑，PyCharm 里报 ModuleNotFound | PyCharm 用的解释器和终端不是同一个 | `Settings → Python Interpreter` 换成同一个 |
| 文件名叫 `python.py` | 会跟标准库抢名字 | 换个名字 |
| 中文报错 `SyntaxError: invalid character` | 用了中文引号 `“”` 或全角括号 | 全部换成英文半角符号 |

## 动手练

1. 建项目，写 `hello_world.py`，输出一句话。
2. 故意改错（比如删掉一个引号），观察 PyCharm 的红色波浪线和终端的 `Traceback`。
3. 在 `>>>` 里直接算 `2 ** 10`，感受交互式环境的便利。
