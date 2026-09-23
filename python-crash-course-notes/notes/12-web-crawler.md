# 12 爬虫笔记

> 🚧 **占位章节**：这里是留给爬虫笔记的位置，内容待补充。
> 前面 1～11 章是蟒蛇书基础知识，从这里开始记爬虫。

## 待填清单（按计划顺序）

- [ ] 爬虫基本流程：请求 → 响应 → 解析 → 存储
- [ ] `requests`：GET / POST、请求头 headers、params、超时、状态码
- [ ] `User-Agent` 与反爬入门：伪装 UA、请求频率、Cookie / Session
- [ ] 解析网页：`BeautifulSoup`（find / find_all、CSS 选择器）、`lxml`、正则 `re`
- [ ] 保存数据：写 CSV / JSON、存数据库
- [ ] 动态页面：接口抓包（XHR / JSON）、`selenium` / `playwright` 入门
- [ ] 图片 / 文件下载
- [ ] 进阶：`Scrapy` 框架、`aiohttp` 异步爬虫
- [ ] 法律与礼仪：`robots.txt`、别把人家网站搞崩

## 环境准备（先记着，之后补内容）

```bash
pip install requests beautifulsoup4 lxml
```

## 最小骨架示例（待补充注释与说明）

```python
import requests

url = "https://example.com"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers, timeout=10)
response.encoding = "utf-8"
print(response.status_code)
print(response.text[:200])
```

## 备忘

- [ ] 抓包工具：浏览器 F12 → Network，优先找 XHR / Fetch 里的 JSON 接口，比解析 HTML 省事
- [ ] 遇到乱码先查 `response.encoding`，再看网页 `<meta charset>`
- [ ] 加 `time.sleep()` 控制频率，别高频请求
- [ ]  robots / 版权 / 隐私：只爬公开、允许爬的数据
