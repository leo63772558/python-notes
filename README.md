# 🐍 Python 编程：从入门到实践（第 3 版）· 学习笔记

> 配套视频：**重磅来袭！超 250 万读者的选择：蟒蛇书《Python 编程：从入门到实践（第 3 版）》，最新版配套视频抢先看**
> 视频 UP 主：B 站 **@林粒粒呀** ｜ 原书作者：Eric Matthes（埃里克·马瑟斯）

这是一份**跟着视频敲一遍、能直接跑起来**的 Markdown 手写笔记，覆盖蟒蛇书第 1～11 章（基础知识部分），
以及第 12 章**爬虫笔记**：`requests` 发请求 → HTML 结构与常用标签 → `BeautifulSoup` 解析 → 豆瓣电影 Top 250 实战（代码已跑通）。
所有代码均在 **Python 3.11+** 下验证，风格跟随第 3 版：f-string 格式化、`pathlib` 读写文件、`pytest` 写测试。

---

## 📑 视频目录 × 笔记索引

| # | 视频小节 | 时长 | 笔记 |
|---|---------|------|------|
| 0 | 介绍篇 | 02:39 | [00 介绍篇](notes/00-intro.md) |
| 1 | 先导篇：为什么安装 Python 和 PyCharm | 01:25 | [01 起步](notes/01-getting-started.md) |
| 1.1–1.2 | 搭建编程环境（macOS 系统） | 04:44 | [01 起步](notes/01-getting-started.md) |
| 1.1–1.2 | 搭建编程环境（Windows 系统） | 04:46 | [01 起步](notes/01-getting-started.md) |
| 1 番外 | 创建 PyCharm 项目 | 04:38 | [01 起步](notes/01-getting-started.md) |
| 2 先导 | 打印 | 06:26 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 2 先导 | 更多打印 | 06:43 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 2.2 | 变量（上） | 02:56 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 2.2 | 变量（下） | 04:49 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 2.3 | 字符串 | 05:35 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 2.4 | 数 | 05:22 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 2.5 | 注释 | 04:08 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 2 番外 | 数据类型 | 06:59 | [02 变量和简单数据类型](notes/02-variables-and-data-types.md) |
| 3.1–3.3 | 列表及列表操作 | 09:06 | [03 列表简介](notes/03-lists.md) |
| 4.1 | 遍历整个列表 | 04:07 | [04 操作列表](notes/04-working-with-lists.md) |
| 4.3 | 创建数值列表 | 04:53 | [04 操作列表](notes/04-working-with-lists.md) |
| 5.2–5.3 | 条件测试与 if 语句 | 02:35 | [05 if 语句](notes/05-if-statements.md) |
| 5.3 | 更多 if 语句 | 06:12 | [05 if 语句](notes/05-if-statements.md) |
| 5 番外 | 逻辑运算 | 02:57 | [05 if 语句](notes/05-if-statements.md) |
| 6.2 | 使用字典 | 06:07 | [06 字典](notes/06-dictionaries.md) |
| 6.3 | 遍历字典 | 04:33 | [06 字典](notes/06-dictionaries.md) |
| 6 番外 | 格式化字符串 | 03:20 | [06 字典](notes/06-dictionaries.md) |
| 7.1 | 函数 input() 的工作原理 | 04:19 | [07 用户输入和 while 循环](notes/07-user-input-and-while.md) |
| 7.2 | while 循环简介 | 05:47 | [07 用户输入和 while 循环](notes/07-user-input-and-while.md) |
| 8.1 | 定义函数 | 05:28 | [08 函数](notes/08-functions.md) |
| 8.3 | 返回值 | 05:23 | [08 函数](notes/08-functions.md) |
| 9 先导 | 搞懂面向对象编程 | 08:45 | [09 类](notes/09-classes.md) |
| 9.1 | 创建和使用类 | 03:54 | [09 类](notes/09-classes.md) |
| 9.2 | 使用类和实例 | 09:31 | [09 类](notes/09-classes.md) |
| 9.3 | 继承 | 07:22 | [09 类](notes/09-classes.md) |
| 10 先导 | 文件路径 | 03:02 | [10 文件和异常](notes/10-files-and-exceptions.md) |
| 10.1 | 读取文件 | 05:46 | [10 文件和异常](notes/10-files-and-exceptions.md) |
| 10.2 | 写入文件 | 05:17 | [10 文件和异常](notes/10-files-and-exceptions.md) |
| 10.3 | 异常 | 07:45 | [10 文件和异常](notes/10-files-and-exceptions.md) |
| 11.1 | 测试函数 | 05:01 | [11 测试代码](notes/11-testing.md) |
| 11.2 | 测试类 | 08:09 | [11 测试代码](notes/11-testing.md) |
| 12 | 爬虫入门 12.1 爬虫是什么 | 03:13 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.2 爬虫流程与法律红线 | 04:07 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.3 HTTP 请求与响应 | 04:37 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.4 requests 发送请求 | 04:24 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.5 实践：拿到豆瓣源码 | 04:18 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.6 HTML 网页结构 | 03:09 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.7 HTML 常用标签 | 05:55 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.8 实践：手写 HTML 页面 | 12:47 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.9 BeautifulSoup 解析 | 07:02 | [12 爬虫笔记](notes/12-web-crawler.md) |
| 12 | 爬虫入门 12.10 实践：豆瓣 Top 250 | 08:51 | [12 爬虫笔记](notes/12-web-crawler.md) |

---

## 📁 仓库结构

```
python-notes/
├── README.md                          ← 你在这里
├── code/
│   ├── douban_top250.py              豆瓣电影 Top250 完整爬虫（可直接跑）
│   └── practice.html                 HTML 标签练习页面（浏览器打开看效果）
└── notes/
    ├── 00-intro.md                    介绍篇：这本书怎么学
    ├── 01-getting-started.md          起步：Python + PyCharm 环境
    ├── 02-variables-and-data-types.md 变量、字符串、数、注释
    ├── 03-lists.md                    列表：增删改查
    ├── 04-working-with-lists.md       遍历、切片、数值列表、推导式
    ├── 05-if-statements.md            条件测试、if 结构、逻辑运算
    ├── 06-dictionaries.md             字典、遍历、嵌套、f-string
    ├── 07-user-input-and-while.md     input()、while 循环
    ├── 08-functions.md                定义函数、参数、返回值、模块
    ├── 09-classes.md                  面向对象：类、实例、继承
    ├── 10-files-and-exceptions.md     pathlib、读写文件、异常处理、json
    ├── 11-testing.md                  pytest：测试函数与测试类
    └── 12-web-crawler.md              爬虫笔记：requests / HTML / BeautifulSoup + 豆瓣 Top250 实战
```

---

## 🧭 第 3 版相对第 2 版的关键变化（必看）

| 主题 | 第 2 版 | 第 3 版 |
|------|---------|---------|
| Python 版本 | 3.7 | **3.11** |
| 推荐编辑器 | Sublime Text | **VS Code**（本套视频用 PyCharm） |
| 文件读写 | `open()` + 字符串路径 | **`pathlib`** |
| 测试 | `unittest` | **`pytest`** |
| 新增字符串方法 | — | **`removeprefix()` / `removesuffix()`** |
| 报错信息 | 简略 | **更精准（带箭头指向出错位置）** |

---

## ⚙️ 本地环境

- Python **3.11+**（`python --version` 查看）
- 编辑器：PyCharm（视频同款）或 VS Code
- 第 11 章需要装第三方库：

```bash
pip install pytest
```

---

## 🚀 推到 GitHub

本仓库已推到：**https://github.com/leo63772558/python-notes**

```bash
cd python-notes
git init
git add .
git commit -m "docs: 蟒蛇书第3版 1-11章笔记"
git branch -M main
git remote add origin git@github.com:leo63772558/python-notes.git
git push -u origin main
```

> 小建议：加一个 `.gitignore`，避免把 `__pycache__/`、`.pytest_cache/`、`.venv/` 传上去。

---

## ✍️ 说明

- 笔记按视频顺序整理，是我跟着敲代码时的理解与补充，**不是书的原文复制**。
- 书籍版权归作者 Eric Matthes 及出版社所有，本仓库仅作个人学习用途。
- 有错漏欢迎提 Issue / PR 一起改。
