# 12 爬虫笔记

> 配套视频：**Python 爬虫入门**（共 10 节，约 60 分钟）
> 主线：`requests` 发请求 → 拿到豆瓣源码 → 学 HTML 结构与常用标签 → `BeautifulSoup` 解析 → 实战豆瓣电影 Top 250
> 本章所有代码都在 **Python 3.13 + requests 2.34 + beautifulsoup4 4.15** 下**实跑验证过**，输出结果是真的。

| # | 视频小节 | 时长 | 对应章节 |
|---|---------|------|---------|
| 1 | 爬虫到底是个啥？ | 03:13 | [12.1](#121-爬虫到底是个啥0313) |
| 2 | 爬虫的流程？从入门到入狱？ | 04:07 | [12.2](#122-爬虫的流程0407) |
| 3 | 什么是 HTTP 请求和响应？ | 04:37 | [12.3](#123-http-请求和响应0437) |
| 4 | 如何用 Python Requests 发送请求？ | 04:24 | [12.4](#124-requests-发送请求0424) |
| 5 | 实践：用 Python Requests 拿到豆瓣源码 | 04:18 | [12.5](#125-实践拿到豆瓣源码0418) |
| 6 | 什么是 HTML 网页结构？ | 03:09 | [12.6](#126-html-网页结构0309) |
| 7 | HTML 有哪些常用标签？ | 05:55 | [12.7](#127-html-常用标签0555) |
| 8 | 实践：练习 HTML 常见标签 | 12:47 | [12.8](#128-实践手写一个-html-页面1247) |
| 9 | 如何用 Beautiful Soup 解析 HTML 内容？ | 07:02 | [12.9](#129-beautifulsoup-解析-html0702) |
| 10 | 实践：从源码获取豆瓣电影 Top 250 | 08:51 | [12.10](#1210-实践豆瓣电影-top-250-全量抓取0851) |

## 12.0 环境准备

```bash
pip install requests beautifulsoup4 lxml
```

| 库 | 干什么 |
|----|--------|
| `requests` | 发 HTTP 请求，把网页「下载」下来（替代浏览器地址栏） |
| `beautifulsoup4` | 解析 HTML，从一堆标签里把想要的数据「抠」出来 |
| `lxml` | 解析器（比内置的 `html.parser` 快很多；不装也能跑，只是慢） |

> 装上就行，先别纠结原理，用到哪学到哪。

---

## 12.1 爬虫到底是个啥？（03:13）

**一句话：爬虫 = 让程序替你「打开网页 → 复制想要的内容 → 存下来」，而且是 7×24 小时不喊累地重复干。**

你平时手动做的事：

```
打开浏览器 → 输入网址 → 看到页面 → 用鼠标选中文字 → Ctrl+C → 粘贴到 Excel
```

爬虫干的事：

```
程序 requests.get(url) → 拿到网页源码（一堆 HTML 文本）→ BeautifulSoup 定位标签 → 提取文字 → 写进 CSV/数据库
```

### 三个类比帮你理解

| 概念 | 类比 |
|------|------|
| `requests` | **你家的浏览器**（负责跑腿，把网页搬回来） |
| HTML 源码 | **搬回来的那堆「带格式的原材料」** |
| `BeautifulSoup` | **你手里的剪刀**（从原材料里剪出想要的那一块） |

### 爬虫能干嘛

- 数据采集：豆瓣电影、招聘信息、房价、天气……批量拿来做分析
- 搜索引擎：百度/谷歌的底层就是超级爬虫（叫 Spider）
- 比价、舆情监控、论文素材收集、自动化测试

### 它不是什么

- ❌ 不是黑客工具：爬虫只是**自动访问公开页面**，不破解、不入侵
- ❌ 不能拿到需要登录才能看的内容（那是另一个性质的问题）
- ❌ 爬不到 App 里的数据（App 走的是接口，得抓包，后面再说）

---

## 12.2 爬虫的流程（04:07）

### 标准五步

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ 1 定目标  │→ │ 2 发请求  │→ │ 3 拿响应  │→ │ 4 解析提取 │→ │ 5 清洗存储 │
│ 爬什么？  │   │ requests │   │ HTML/JSON│   │   bs4     │   │ CSV/JSON  │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
                     ↑                                            │
                     └──────────── 6 翻页 / 循环 ←────────────────┘
```

展开说：

1. **定目标**：去哪个 URL、要哪些字段（先看人家的网页长啥样，F12 看结构）
2. **发请求**：`requests.get(url, headers=...)`
3. **拿响应**：拿到的是**字符串**（HTML 文本）或 JSON
4. **解析提取**：`BeautifulSoup` + CSS 选择器定位到标签，取文本
5. **清洗存储**：去掉多余空白、转类型，写成 CSV / JSON / 数据库
6. **翻页**：找到分页规律（`start=0, 25, 50...`），循环 1～5

### ⚖️ 「从入门到入狱」：红线在哪（这节必看）

教程标题是调侃，但真有人因为爬虫进去过。记住下面几条，你这辈子都安全：

**✅ 安全的做法：**

- 只爬**公开可见**、不需要登录的数据
- 先看 `robots.txt`（网站根目录，比如 `https://www.douban.com/robots.txt`），人家明说不能爬的目录就别碰
- **控制频率**：`time.sleep(1)` 是基本礼貌，别一秒几百次把人家服务器干趴
- 加 `timeout`，别让对方等半天
- 数据**自己学习分析用**，别打包转卖、别原样转载传播
- 尊重版权：爬来的文章/图片不要当成自己的发出去

**❌ 会出事的做法：**

| 行为 | 风险 |
|------|------|
| 爬**需要登录**才能看的内容（个人信息、订单、后台数据） | 可能构成「非法获取计算机信息系统数据罪」 |
| 绕过/破解验证码、加密接口、反爬机制 | 性质从「爬」变成「侵入」 |
| 高频并发请求导致对方服务瘫痪 | 「破坏计算机信息系统罪」 |
| 爬公民个人信息并出售/提供 | 「侵犯公民个人信息罪」 |
| 把爬来的付费内容公开传播 | 民事侵权 + 版权问题 |

> 相关法律：《网络安全法》《数据安全法》《个人信息保护法》《刑法》第 285/286 条。
> **一句话底线：爬公开数据 + 慢一点 + 自己用 = 学习；爬隐私数据 + 破反爬 + 拿去卖 = 犯罪。**

---

## 12.3 HTTP 请求和响应（04:37）

HTTP = 浏览器和服务器**说话的规矩**。你发一句「我要这个页面」，服务器回一句「给你 / 不给你」。

### URL 长什么样

```
https://movie.douban.com/top250?start=25&filter=
└─┬──┘  └───────┬───────┘└─┬─┘ └───────┬───────┘
 协议          域名        路径       查询参数（?key=value&key2=value2）
```

### 请求（Request）：你发给服务器的

```
GET /top250?start=25 HTTP/1.1        ← 请求行：方法 + 路径 + 协议
Host: movie.douban.com               ← 请求头开始
User-Agent: Mozilla/5.0 ...          ← 我是谁（浏览器身份）
Cookie: bid=xxx; ...                 ← 登录凭证
Accept: text/html
                                     ← 空行
                                     ← 请求体（GET 一般为空，POST 才放数据）
```

| 请求方法 | 含义 | 数据放哪 |
|---------|------|---------|
| **GET** | 要数据（最常见，爬虫 90% 用它） | URL 的查询参数里 |
| **POST** | 提交数据（登录、表单、搜索） | 请求体 body 里 |
| PUT / DELETE | 改 / 删（REST API 用） | body 里 |
| HEAD | 只要响应头，不要内容 | — |

**爬虫最常打交道的请求头：**

| 头 | 作用 |
|----|------|
| `User-Agent` | **最重要**。告诉服务器你是什么浏览器。不伪装就是爬虫（见 12.5 的 418） |
| `Cookie` | 登录状态 |
| `Referer` | 从哪个页面跳过来的（防盗链会查） |
| `Accept` | 我能接受什么格式 |
| `Content-Type` | POST 时数据的格式 |

### 响应（Response）：服务器回给你的

```
HTTP/1.1 200 OK                      ← 状态行：协议 + 状态码 + 说明
Content-Type: text/html; charset=utf-8 ← 响应头
Set-Cookie: ...
                                     ← 空行
<!DOCTYPE html><html>...             ← 响应体：真正的 HTML 源码
```

**状态码必须背下来：**

| 状态码 | 含义 | 爬虫遇到怎么办 |
|--------|------|--------------|
| **200** | 成功 ✅ | 正常解析 |
| 301 / 302 | 重定向 | `requests` 默认自动跟随，一般不用管 |
| 400 | 请求有问题 | 检查参数 |
| **401** | 未登录 | 要带 Cookie / 登录 |
| **403** | 被拒绝（常见反爬） | 补 UA、Referer、Cookie |
| **404** | 页面不存在 | URL 写错了 |
| **418** | 我是茶壶 🫖（彩蛋，**豆瓣用它挡爬虫**） | 加浏览器 UA |
| **429** | 请求太频繁，被限流 | `sleep` 慢一点 |
| 500 / 502 / 503 | 服务器炸了 | 过会儿重试 |

> 补充：**HTTP 是无状态的**——服务器记不住你上一步干过啥，所以才有 Cookie / Session 来「记住你是谁」。

---

## 12.4 requests 发送请求（04:24）

### 最小示例

```python
import requests

response = requests.get("https://movie.douban.com/top250")
print(response.status_code)   # 状态码
print(response.text)          # 响应体（字符串）
```

### Response 对象常用属性

| 属性 | 返回什么 |
|------|---------|
| `r.status_code` | 状态码（int），200 就是成功 |
| `r.text` | 响应内容（**字符串**，按 `r.encoding` 解码） |
| `r.content` | 响应内容（**字节 bytes**，下载图片/视频用这个） |
| `r.encoding` | 当前编码；乱码就改它：`r.encoding = "utf-8"` |
| `r.apparent_encoding` | 程序猜的编码（猜不准时参考） |
| `r.headers` | 响应头（字典） |
| `r.cookies` | 服务器给的 Cookie |
| `r.url` | 最终请求的 URL（看参数拼对没） |
| `r.json()` | 响应是 JSON 时，直接转成字典/列表 |
| `r.raise_for_status()` | 状态码不是 200 就抛异常（**推荐加上**） |

### 四个必会参数

```python
r = requests.get(
    url,
    params={"start": 25},          # ① 查询参数，自动拼成 ?start=25
    headers={"User-Agent": "..."}, # ② 请求头，伪装成浏览器
    timeout=10,                    # ③ 超时秒数，必写！否则可能永久卡住
    cookies={"bid": "xxx"},        # ④ Cookie（也可以放进 headers）
)
```

**写代码别手拼 URL**：

```python
# ❌ 麻烦还容易错
requests.get("https://movie.douban.com/top250?start=" + str(25))
# ✅ 用 params
requests.get("https://movie.douban.com/top250", params={"start": 25})
```

### POST 请求

```python
# 表单格式（网页表单常见）
requests.post("https://httpbin.org/post", data={"user": "admin", "pwd": "123"})

# JSON 格式（现在大多数接口用这个）
requests.post("https://httpbin.org/post", json={"user": "admin", "pwd": "123"})
```

### Session：保持会话（要登录时用它）

```python
session = requests.Session()          # 自动帮你保存/带上 Cookie
session.headers.update({"User-Agent": "Mozilla/5.0"})
session.post(login_url, data={"user": "a", "pwd": "b"})   # 登录
r = session.get(profile_url)          # 带着登录状态访问
```

### 异常处理（别让程序一崩全没）

```python
import requests

try:
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()               # 4xx / 5xx 直接抛错
except requests.exceptions.Timeout:
    print("超时了")
except requests.exceptions.HTTPError as e:
    print("状态码有问题：", e)
except requests.exceptions.RequestException as e:
    print("请求失败：", e)
```

> 常见坑：忘记 `timeout` → 网络不好时程序卡死不动；忘记 `raise_for_status()` → 拿到 403 页面还在那解析，结果啥也没有。

---

## 12.5 实践：拿到豆瓣源码（04:18）

### 第一步：先别伪装，看看会发生什么

```python
import requests

r = requests.get("https://movie.douban.com/top250", timeout=10)
print(r.status_code)   # 418  ← 被识破了！
print(len(r.text))     # 0    ← 内容都是空的
```

**418 I'm a teapot**：豆瓣发现你是 `python-requests`（默认 UA 里明写着），直接拒绝，返回空内容。
这就是新手最常见的「为啥我爬下来是空的」——**不是代码错，是被反爬了**。

### 第二步：加浏览器 User-Agent

UA 怎么来？浏览器 F12 → Network → 点任意请求 → Request Headers 里抄 `User-Agent`。

```python
import requests

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers, timeout=10)
r.encoding = "utf-8"                  # 显式指定编码，防乱码

print(r.status_code)                  # 200 ✅
print(len(r.text))                    # 60000+ 字符，源码到手
print(r.text[:500])                   # 打印前 500 个字符看看
```

### 第三步：把源码存成文件（方便反复分析）

```python
with open("douban_top250.html", "w", encoding="utf-8") as f:
    f.write(r.text)
```

存下来之后用浏览器打开、或者拖进 PyCharm 慢慢看结构，**比每次都重新请求省事得多，也不打扰人家服务器**。

> 💡 调试小技巧：第一次开发解析代码时，读本地 HTML 文件：
> ```python
> soup = BeautifulSoup(open("douban_top250.html", encoding="utf-8").read(), "lxml")
> ```
> 解析逻辑调通了，再换成发请求。

---

## 12.6 HTML 网页结构（03:09）

HTML = **用标签描述的树形文档**。浏览器把它渲染成你看到的漂亮页面，爬虫看到的则是这棵树。

### 骨架

```html
<!DOCTYPE html>                  ← 声明：这是 HTML5
<html lang="zh-CN">              ← 根元素（整棵树只有一个）
<head>                           ← 头部：给浏览器看的，页面上不显示
    <meta charset="utf-8">       ←   编码
    <title>豆瓣电影 Top 250</title>  ←   浏览器标签页上的标题
    <link rel="stylesheet" href="style.css">
</head>
<body>                           ← 身体：页面上能看到的一切都在里面
    <h1>豆瓣电影 Top 250</h1>
    <p>这是一段文字</p>
</body>
</html>
```

### 四个基本概念

| 概念 | 说明 | 例子 |
|------|------|------|
| **标签 tag** | 尖括号包起来的关键字，成对出现 | `<p>内容</p>` |
| **属性 attribute** | 写在开始标签里，描述标签的额外信息 | `<a href="url">` 的 `href` |
| **文本 text** | 标签之间的内容，就是你要爬的数据 | `<p>文字</p>` |
| **嵌套** | 标签套标签，形成父子/兄弟关系 | `<div><p>x</p></div>` |

```
html
├── head
│   ├── meta
│   └── title
└── body
    ├── h1
    └── div
        ├── p
        └── a
```

> 爬虫里最关键的三个属性：**`class`**（一类元素的标记，可重复）、**`id`**（唯一标识）、**`href`/`src`**（链接地址）。

自闭合标签（没有结束标签）：`<img>` `<br>` `<hr>` `<input>` `<meta>`。

---

## 12.7 HTML 常用标签（05:55）

| 标签 | 作用 | 爬虫视角 |
|------|------|---------|
| `<h1>` ~ `<h6>` | 标题，h1 最大 | 常用来抓文章标题 |
| `<p>` | 段落 | 正文内容 |
| `<a href="...">` | 超链接 | ⭐ **抓链接全靠它的 `href`** |
| `<img src="...">` | 图片 | ⭐ **下载图片找 `src`** |
| `<ul>` / `<ol>` / `<li>` | 无序/有序列表 + 列表项 | ⭐ **列表型数据（排行榜、商品）** |
| `<div>` | 块级容器（布局用） | 最大的分组单位 |
| `<span>` | 行内容器 | 小段文字、评分、数字 |
| `<table>` / `<tr>` / `<td>` / `<th>` | 表格 / 行 / 单元格 / 表头 | 表格数据最好爬 |
| `<strong>` / `<em>` | 加粗 / 斜体 | 强调内容 |
| `<br>` / `<hr>` | 换行 / 分隔线 | 解析时 `get_text()` 要处理 |
| `<form>` / `<input>` / `<button>` | 表单 / 输入框 / 按钮 | 模拟登录、搜索要用 |
| `<meta>` | 元信息（编码、描述） | 判断编码用 |
| `<script>` / `<style>` | JS 脚本 / CSS 样式 | ⚠️ 一般**不要**从这里取数据 |
| `<!-- 注释 -->` | 注释 | 不显示 |

### 属性速查

| 属性 | 用途 | 常见于 |
|------|------|--------|
| `id="x"` | 唯一标识（一个页面不能重复） | 定位单个元素 |
| `class="x y"` | 分类标记（**可多个、可重复**） | ⭐ 爬虫定位的主力 |
| `href="url"` | 链接地址 | `<a>` |
| `src="url"` | 资源地址 | `<img>` `<script>` |
| `alt="文字"` | 图片加载失败时的替代文字 | `<img>` |
| `title="文字"` | 鼠标悬停提示 | 任意标签 |
| `data-xxx="值"` | 自定义数据 | 很多网站把数据藏这里 |

> ⭐ **爬虫实战口诀**：想拿文字就找**标签 + class**，想拿链接就找 **`a` 的 `href`**，想拿图片就找 **`img` 的 `src`**。

---

## 12.8 实践：手写一个 HTML 页面（12:47）

为什么要手写？**你得知道标签怎么嵌套，才能猜到别人页面的结构、写出正确的选择器。**

把下面这段存成 `practice.html`，双击用浏览器打开看看效果（配套文件在 `code/practice.html`）：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>我的电影清单</title>
</head>
<body>
    <h1>我喜欢的电影</h1>
    <p>下面是我的 <strong>Top 3</strong>，评分来自豆瓣。</p>

    <h2>排行榜</h2>
    <ol class="movie-list">
        <li class="item">
            <span class="rank">1</span>
            <a href="https://movie.douban.com/subject/1292052/">肖申克的救赎</a>
            <span class="rating">9.7</span>
        </li>
        <li class="item">
            <span class="rank">2</span>
            <a href="https://movie.douban.com/subject/1291546/">霸王别姬</a>
            <span class="rating">9.6</span>
        </li>
        <li class="item">
            <span class="rank">3</span>
            <a href="https://movie.douban.com/subject/1292720/">阿甘正传</a>
            <span class="rating">9.5</span>
        </li>
    </ol>

    <h2>海报</h2>
    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2934829882.jpg"
         alt="肖申克的救赎海报" width="120">

    <h2>信息表</h2>
    <table>
        <tr><th>电影</th><th>年份</th><th>评分</th></tr>
        <tr><td>肖申克的救赎</td><td>1994</td><td>9.7</td></tr>
        <tr><td>霸王别姬</td><td>1993</td><td>9.6</td></tr>
    </table>

    <!-- 这是注释，浏览器不会显示 -->
</body>
</html>
```

### 练完自己答一遍（检验真懂了没）

1. 页面里有几个 `class="item"` 的元素？→ 3 个（class 可重复，所以要用 `select` 拿全部）
2. 要抓所有电影名，CSS 选择器怎么写？→ `.movie-list .item a`
3. 要抓评分呢？→ `.item .rating`
4. `img` 的链接在哪个属性里？→ `src`
5. `table` 里表头用的是哪个标签？→ `<th>`（普通单元格是 `<td>`）

### 再用 BeautifulSoup 解析自己写的页面

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("practice.html", encoding="utf-8").read(), "lxml")
for item in soup.select(".movie-list .item"):
    rank = item.select_one(".rank").get_text(strip=True)
    name = item.select_one("a").get_text(strip=True)
    link = item.select_one("a")["href"]
    rating = item.select_one(".rating").get_text(strip=True)
    print(f"{rank}. {name} | {rating} | {link}")
```

输出：

```
1. 肖申克的救赎 | 9.7 | https://movie.douban.com/subject/1292052/
2. 霸王别姬 | 9.6 | https://movie.douban.com/subject/1291546/
3. 阿甘正传 | 9.5 | https://movie.douban.com/subject/1292720/
```

> 先在自己写的干净 HTML 上练选择器，再去啃豆瓣那种真实页面，难度直接降一个档。

---

## 12.9 BeautifulSoup 解析 HTML（07:02）

### 三步走

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_text, "lxml")   # ① 造一碗汤（html_text 是字符串）
tag = soup.select_one(".title")           # ② 定位到标签
text = tag.get_text(strip=True)           # ③ 取文本
```

解析器选哪个：

| 写法 | 速度 | 说明 |
|------|------|------|
| `"lxml"` | 快 ✅ | **推荐**，需 `pip install lxml` |
| `"html.parser"` | 中等 | Python 自带，不用装 |
| `"html5lib"` | 慢 | 容错最强，HTML 写得很烂时用 |

### 找元素两种方式：`find` 系列 和 CSS 选择器

| 目的 | `find` 写法 | CSS 选择器写法（推荐） |
|------|------------|---------------------|
| 找**第一个** | `soup.find("div", class_="item")` | `soup.select_one("div.item")` |
| 找**所有** | `soup.find_all("li")` | `soup.select("ol.grid_view li")` |

> 个人建议：**优先用 `select` / `select_one`**。因为浏览器 F12 里可以直接右键「Copy selector」，抄过来就能用，不用记 `class_` 这种下划线的怪写法。

### CSS 选择器语法速查（够用了）

| 选择器 | 含义 | 例子 |
|--------|------|------|
| `div` | 标签名 | `soup.select("div")` |
| `.cls` | class | `.item` → class 含 item |
| `#id` | id | `#content` |
| `a b`（空格） | 后代（b 在 a 里面，任意层级） | `ol li` |
| `a > b` | 直接子元素 | `ol > li` |
| `tag.cls` | 标签 + class | `span.title` |
| `[attr]` / `[attr="v"]` | 按属性找 | `a[href]`、`img[src$=".jpg"]` |

### 拿到标签之后

```python
tag = soup.select_one("a")

tag.get_text()                 # 标签里的文本（含子孙）
tag.get_text(strip=True)       # 去掉首尾空白 ⭐常用
tag.get_text(" ", strip=True)  # 用空格连接多段文本（处理 <br> 换行）⭐

tag["href"]                    # 取属性（没有就 KeyError）
tag.get("href")                # 取属性（没有返回 None）⭐更安全
tag.get("href", "默认值")       # 没有就用默认值

tag.name                       # 标签名，如 'a'
tag.attrs                      # 所有属性组成的字典
```

### 实战里的常用组合

```python
# 1. 找到列表容器，再遍历每一项（最常用套路）
for item in soup.select("ol.grid_view li"):
    ...

# 2. 按 class 找，注意 Python 里要写 class_（下划线！因为 class 是关键字）
soup.find_all("span", class_="title")     # class 是关键字，必须加下划线

# 3. 按多个条件 / 属性
soup.find_all("div", attrs={"class": "item"})
soup.find_all("img", attrs={"data-type": "photo"})

# 4. 只要前 N 个
soup.find_all("li", limit=5)

# 5. 文本内容是 None 的判断（有的条目没有某个字段！）
quote = soup.select_one("p.quote span")
text = quote.get_text(strip=True) if quote else ""     # ⭐ 一定要判空
```

> ⚠️ **最容易踩的坑**：不是每个条目的结构都一样。有的电影没有引言、有的没有外文名，
> 直接 `.get_text()` 会报 `AttributeError: 'NoneType' object has no attribute 'get_text'`。
> **先 `select_one` 拿到对象，判断不为 None 再取值。**

### 调试技巧：不确定结构就打印出来看

```python
print(soup.prettify()[:2000])        # 格式化打印前 2000 字符
print(soup.select("ol.grid_view li")[0].prettify())   # 只看第一个条目的结构
```

---

## 12.10 实践：豆瓣电影 Top 250 全量抓取（08:51）

### 先摸清页面结构（F12 是关键）

在浏览器打开 `https://movie.douban.com/top250`，F12 看源码，每个电影是一个 `<li>`：

```html
<li>
  <div class="item">
    <div class="pic">
      <em>1</em>                                    <!-- 排名 -->
      <a href="https://movie.douban.com/subject/1292052/">
        <img src="..." alt="肖申克的救赎">           <!-- 海报 -->
      </a>
    </div>
    <div class="info">
      <div class="hd">
        <a href="...">
          <span class="title">肖申克的救赎</span>      <!-- 中文名 -->
          <span class="title">/ The Shawshank Redemption</span>  <!-- 外文名 -->
          <span class="other">/ 月黑高飞(港) / 刺激1995(台)</span> <!-- 别名 -->
        </a>
      </div>
      <div class="bd">
        <p>导演: xxx   主演: xxx <br> 1994 / 美国 / 犯罪 剧情</p>
        <div>
          <span class="rating_num">9.7</span>        <!-- 评分 -->
          <span>3343540人评价</span>                  <!-- 评价人数 -->
        </div>
        <p class="quote"><span>希望让人自由。</span></p> <!-- 一句话引言 -->
      </div>
    </div>
  </div>
</li>
```

**字段 ↔ 选择器对照表**（实测于 2026-09，豆瓣改版后老教程里的 `div.star`、`span.inq` 已经**不存在**了，别照抄旧博客）：

| 字段 | CSS 选择器 | 备注 |
|------|-----------|------|
| 排名 | `div.pic em` | |
| 中文名 | `div.hd span.title` | 取**第一个** |
| 外文名 | 第 2 个 `div.hd span.title` | 有的条目没有 |
| 别名 | `span.other` | |
| 详情页链接 | `div.hd a` 的 `href` | |
| 海报 | `div.pic img` 的 `src` | |
| 评分 | `span.rating_num` | |
| 评价人数 | `div.bd div span` 里含「人评价」的 | 用正则 `(\d+)人评价` |
| 一句话引言 | `p.quote span` | ⚠️ 不是 `span.inq`，且**可能没有** |
| 导演/年份/类型 | `div.bd p` | 用 `get_text(" ", strip=True)` |

### 翻页规律

```
第1页：https://movie.douban.com/top250?start=0
第2页：?start=25
...
第10页：?start=225
```

**共 10 页 × 25 条 = 250 条电影。** 用 `params={"start": start}` 传就行。

### 完整代码（可直接跑，已验证）

配套文件：`code/douban_top250.py`

```python
"""豆瓣电影 Top 250 爬虫：requests 发请求 + BeautifulSoup 解析 + 存 CSV/JSON"""
import csv
import json
import re
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://movie.douban.com/top250"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
FIELDS = ["rank", "name", "en_name", "other_name", "rating", "votes", "quote", "info", "url", "poster"]


def fetch_page(start):
    """发请求，拿到一页的 HTML 源码"""
    response = requests.get(BASE_URL, params={"start": start, "filter": ""},
                            headers=HEADERS, timeout=10)
    response.raise_for_status()          # 不是 200 就直接报错，别往下走
    response.encoding = "utf-8"          # 显式指定编码，防止中文乱码
    return response.text


def parse_page(html):
    """从一页 HTML 里解析出 25 部电影"""
    soup = BeautifulSoup(html, "lxml")
    for item in soup.select("ol.grid_view li"):
        # 电影名可能有多个 span.title（中文名 + 外文名）
        titles = [s.get_text(strip=True) for s in item.select("div.hd span.title")]
        name = titles[0]
        en_name = titles[1].lstrip("/ ").strip() if len(titles) > 1 else ""

        other_tag = item.select_one("span.other")
        other_name = other_tag.get_text(strip=True).lstrip("/ ").strip() if other_tag else ""

        # 评价人数：在 div.bd 下的 span 里找「xxx人评价」
        votes = ""
        for span in item.select("div.bd div span"):
            match = re.search(r"(\d+)\s*人评价", span.get_text())
            if match:
                votes = match.group(1)
                break

        # 引言：有的电影没有，必须先判空！
        quote_tag = item.select_one("p.quote span")
        quote = quote_tag.get_text(strip=True) if quote_tag else ""

        yield {
            "rank": item.select_one("div.pic em").get_text(strip=True),
            "name": name,
            "en_name": en_name,
            "other_name": other_name,
            "rating": item.select_one("span.rating_num").get_text(strip=True),
            "votes": votes,
            "quote": quote,
            "info": item.select_one("div.bd p").get_text(" ", strip=True),
            "url": item.select_one("div.hd a")["href"],
            "poster": item.select_one("div.pic img")["src"],
        }


def save(movies):
    """存成 CSV 和 JSON 两种格式"""
    with open("douban_top250.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(movies)

    with open("douban_top250.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)


def main():
    movies = []
    for start in range(0, 250, 25):                 # 0, 25, 50, ... 225
        page = list(parse_page(fetch_page(start)))
        movies.extend(page)
        print(f"已抓取 start={start}，本页 {len(page)} 条，累计 {len(movies)} 条")
        time.sleep(1)                               # ⭐ 慢一点，做个有礼貌的爬虫

    save(movies)
    print(f"\n完成！共 {len(movies)} 部电影 → douban_top250.csv / douban_top250.json")

    print("\nTop 5：")
    for movie in movies[:5]:
        print(f'{movie["rank"]}. {movie["name"]} | {movie["rating"]} | {movie["votes"]}人评价 | {movie["quote"]}')


if __name__ == "__main__":
    main()
```

### 实际输出结果（真跑出来的）

```
已抓取 start=0，本页 25 条，累计 25 条
已抓取 start=25，本页 25 条，累计 50 条
...
已抓取 start=225，本页 25 条，累计 250 条

完成！共 250 部电影 → douban_top250.csv / douban_top250.json

Top 5：
1. 肖申克的救赎 | 9.7 | 3343546人评价 | 希望让人自由。
2. 霸王别姬 | 9.6 | 2455168人评价 | 风华绝代。
3. 泰坦尼克号 | 9.5 | 2532487人评价 | 失去的才是永恒的。
4. 阿甘正传 | 9.5 | 2459477人评价 | 一部美国近现代史。
5. 千与千寻 | 9.4 | 2571395人评价 | 最好的宫崎骏，最好的久石让。
```

> 榜单和评价人数随时在变（我这次跑的时候阿甘正传在第 4），你跑出来的数字跟上面不一样是正常的。

CSV 用 Excel 打开的效果（`utf-8-sig` 编码是为了让 Excel 不乱码）：

```
rank,name,rating
1,肖申克的救赎,9.7
2,霸王别姬,9.6
```

### 这段代码里值得抄走的点

| 技巧 | 为什么 |
|------|--------|
| `params={...}` 而不是拼字符串 | 自动处理转义，不容易写错 |
| `timeout=10` | 网络卡住不会永远等 |
| `raise_for_status()` | 拿到 403/418 立刻报错，而不是解析一堆空内容 |
| `response.encoding = "utf-8"` | 防中文乱码 |
| `time.sleep(1)` | ⭐ 限速，既是礼貌也是自保 |
| `select_one(...) if ... else ""` | 字段可能缺失，判空防崩 |
| 拆成 `fetch` / `parse` / `save` 三个函数 | 结构清晰，改起来容易 |
| `csv` 用 `utf-8-sig` | Excel 打开中文不乱码 |

### 爬下来之后还能干啥（练手）

- 用 `pandas` 读 CSV，算平均分、画评分分布直方图
- 找出评分最高的 10 部、评价人数最多的 10 部
- 按年份统计（从 `info` 字段里正则提取 `\d{4}`）
- 把海报批量下载下来（`requests.get(poster).content` 存成 `.jpg`）

---

## 12.11 常见坑 & 排查清单

| 现象 | 原因 | 解决 |
|------|------|------|
| 返回 **418** / 空内容 | 被反爬，UA 太假 | 换浏览器 User-Agent |
| 返回 **403** | 同上，或需要 Referer | 补 `Referer`、`Cookie` |
| 中文乱码 | 编码判断错了 | `r.encoding = "utf-8"`，或看 `<meta charset>` |
| `AttributeError: 'NoneType'` | 选择器没匹配到（页面结构变了 / 该字段不存在） | 先 `print(soup.prettify())` 看真实结构，再判空 |
| 只爬到 25 条 | 没翻页 | `start` 参数循环 0～225 |
| 爬着爬着被封 | 频率太高 | `time.sleep(1)`，别并发猛砸 |
| 数据是空的，但源码里有 | 数据在 `<script>` 里 / 是 JS 动态渲染的 | ① F12 → Network → 找 XHR/Fetch 的 JSON 接口直接请求；② 用 `selenium` / `playwright` 渲染后再取 |
| 程序卡死不动 | 没设 `timeout` | `requests.get(..., timeout=10)` |

### 下一步学什么

- [ ] 抓包找 JSON 接口（F12 → Network → Fetch/XHR），**比解析 HTML 省事十倍**
- [ ] `selenium` / `playwright`：对付 JS 动态渲染的页面
- [ ] 图片 / 文件批量下载
- [ ] 数据入 MySQL / MongoDB，或用 `pandas` 做分析
- [ ] `Scrapy` 框架：项目大了用它管理
- [ ] 异步 `aiohttp` + `asyncio`：提速

---

## 动手练

1. 不带 UA 请求豆瓣，亲眼看看 **418** 长什么样，再加 UA 对比。
2. 把 `code/practice.html` 手写一遍，加一个 `<table>` 和一张图片。
3. 改 Top 250 的代码，只保留「排名 + 片名 + 评分」三个字段，存成 CSV。
4. 进阶：把 250 部电影的海报全部下载到 `posters/` 目录（记得 `sleep`）。
5. 思考题：如果豆瓣要求登录后才能看第 250 名之后的内容，你还该继续爬吗？（答案见 12.2 红线表）
