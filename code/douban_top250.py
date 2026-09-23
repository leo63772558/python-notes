"""豆瓣电影 Top 250 爬虫：requests 发请求 + BeautifulSoup 解析 + 存 CSV/JSON

用法：
    pip install requests beautifulsoup4 lxml
    python douban_top250.py

产出：douban_top250.csv、douban_top250.json（生成在当前目录）
"""
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
        time.sleep(1)                               # 慢一点，做个有礼貌的爬虫

    save(movies)
    print(f"\n完成！共 {len(movies)} 部电影 → douban_top250.csv / douban_top250.json")

    print("\nTop 5：")
    for movie in movies[:5]:
        print(f'{movie["rank"]}. {movie["name"]} | {movie["rating"]} | {movie["votes"]}人评价 | {movie["quote"]}')


if __name__ == "__main__":
    main()
