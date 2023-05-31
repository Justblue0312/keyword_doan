import newspaper
from goose3 import Goose
import requests
from bs4 import BeautifulSoup
from typing import List


def get_category_news_link(url: str) -> list:
    vnnews = newspaper.build(url)
    pages = []

    for item in vnnews.category_urls():
        pages.append(item)

    for page in pages:
        if page == url or page == url[0:-1]:
            pages.remove(page)

    return pages


def get_news_posts(cate_links: List[str]) -> list:
    hot_news = []

    for link in cate_links:
        vnnews = newspaper.build(link)
        for article in vnnews.articles:
            hot_news.append(article.url)

    for new in list(set(hot_news)):
        if "#box_comment" in new:
            hot_news.remove(new)

    return hot_news


def get_post_info(hot_news: list) -> list:
    post_infos = list()
    for new in hot_news:
        url = new
        g = g = Goose({"browser_user_agent": "Mozilla", "parser_class": "soup"})
        article = g.extract(url=url)

        req = requests.get(url)

        soup = BeautifulSoup(req.content, "html.parser")

        content = soup.find_all("p", attrs={"class": "Normal"})

        new_content = list()
        for item in content:
            new_content.append(str(item.text + " "))

        text_content = "".join(new_content)

        infos = article.infos

        post_info = {
            "title": article.title,
            "author": "VnExpress",
            "intro": article.meta_description,
            "url": infos["opengraph"]["url"],
            "keywords": article.meta_keywords,
            "content": text_content,
            "image": infos["opengraph"]["image"],
            "published_date": infos["publish_date"],
        }
        post_infos.append(post_info)

    return post_infos
