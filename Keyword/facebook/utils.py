from facebook_page_scraper import Facebook_scraper
import ast
import yake
from ..const import STOPWORDS
from typing import List


def getFbPostList(
    request, page_name: str, count: int = 5, browser: str = "chrome"
) -> list:
    facebook_ai = Facebook_scraper(page_name, count, browser)
    json_data = facebook_ai.scrap_to_json()
    json_data = ast.literal_eval(json_data)
    fb_posts = list()
    for _, value in json_data.items():
        value["likes"] = value["reactions"]["likes"]
        value["loves"] = value["reactions"]["loves"]
        value["wow"] = value["reactions"]["wow"]
        value["sad"] = value["reactions"]["sad"]
        value["angry"] = value["reactions"]["angry"]
        value["haha"] = value["reactions"]["haha"]
        value["cares"] = value["reactions"]["cares"]
        del value["reactions"]
        if len(value["image"]) >= 1:
            value["image"] = value["image"][0]

        fb_posts.append(value)

    return fb_posts


def getKeyword(request, text: str) -> List[str]:
    stopwords = STOPWORDS
    kw_extractor = yake.KeywordExtractor(lan="vi", n=2, stopwords=stopwords)
    keywords = kw_extractor.extract_keywords(text)

    kw_list = list()
    for kw in keywords:
        kw_list.append(kw)

    return kw_list
