import requests
from bs4 import BeautifulSoup
import json
from goose3 import Goose
import dateutil.parser


def get_news_posts(url):
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    response = json.loads(response.text)
    next_page_url = response['nextPageUrl']

    article_list = list()
    weather_list = list()
    slide_list = list()

    card_list = list()
    for section in response['sections']:
        cards = section['cards']
        for card in cards:
            if card['type'] == 'infopane':
                card_list.append(card)
            if card['type'] == 'article':
                article_list.append(card)
            if card['type'] == 'WeatherSummary':
                weather_list.append(card)
            if card['type'] == 'slideshow':
                slide_list.append(card)

    if card_list:
        for subCard in card_list[0]['subCards']:
            if subCard['type'] == 'article':
                article_list.append(subCard)

    return next_page_url, article_list, weather_list, slide_list


def get_msn_infos_from_url(url):
    g = Goose()
    article = g.extract(url=url)

    infos = article.infos
    return infos


def get_msn_content_from_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    paragraphs = soup.find_all('p')

    paragraph = ''
    for para in paragraphs[:-1]:
        paragraph += '\n' + para.text + '\n'

    return paragraph


def get_msn_url_from_body_html(body_html):
    soup = BeautifulSoup(str(body_html), 'html.parser')
    url = soup.find('a').get('href')
    return url


def convert_datetime(datetime_string):
    if datetime_string:
        convert = dateutil.parser.parse(str(datetime_string))
        return convert
    else:
        return None
