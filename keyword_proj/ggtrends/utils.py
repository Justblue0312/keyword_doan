import json
from pytrends.request import TrendReq
import html
import requests
from google_searching import ggl
import re
from urllib.parse import unquote
from keyword_proj.const import GGT_API_1, GGT_API_2

pytrend = TrendReq()


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def trendSearch(request):
    trending_df = pytrend.trending_searches(pn='vietnam')
    trend_table = trending_df.reset_index().to_json(orient='records')
    trend_data = []
    trend_data = json.loads(trend_table)

    for item in trend_data:
        item['index'] = item['index'] + 1

    return trend_data


def todayTrend(request):
    today_df = pytrend.today_searches(pn='VN')
    today_table = today_df.reset_index().to_json(orient='records')
    today_trend = []
    today_trend = json.loads(today_table)

    for item in today_trend:
        item['index'] = item['index'] + 1
        per = item['exploreLink'].find('%')
        if per > 0:
            item['exploreLink'] = urllib.parse.unquote(find_between(item['exploreLink'], "/trends/explore?q=",
                                                                    "&date=now+7-d&geo=VN").replace(
                "+", " "))

        else:
            item['exploreLink'] = find_between(item['exploreLink'], "/trends/explore?q=",
                                               "&date=now+7-d&geo=VN").replace(
                "+", " ")

    return today_trend


def todayTrendList(request):
    today_trends = todayTrend(request)
    titles_list = []
    for item in today_trends:
        title = item.get('exploreLink')
        titles_list.append(title)

    return titles_list


def getTheLastFiveYearsTrend(request, year):
    trendList = []
    for i in range(1, 7):
        year -= 1
        top_charts_df = pytrend.top_charts(year, hl='en-US', tz=300, geo='VN')
        top_charts_json = top_charts_df.reset_index().to_json(orient='records')
        trend_table = dict()
        trend_table[year] = json.loads(top_charts_json)
        trendList.append(trend_table)

    return trendList


def getTheLastFiveYearsTrendDict(request, year):
    trendList = []
    for i in range(1, 6):
        year -= 1
        top_charts_df = pytrend.top_charts(year, hl='en-US', tz=300, geo='VN')
        top_charts_json = top_charts_df.reset_index().to_json(orient='records')
        trend_table = dict()
        trend_table[year] = json.loads(top_charts_json)
        trendList.append(trend_table)

    for item in trendList:
        for key, value in item.items():
            for i in value:
                i['index'] = i['index'] + 1

    h_list = list()

    for item in trendList:
        for key, value in item.items():
            h = {
                'year_trend': key,
                'trends': list()
            }
            for i in value:
                h['trends'].append(i.get('title'))
        h_list.append(h)

    return h_list


def trendCategories(request):
    category = pytrend.categories()

    cate_dict = dict()
    for i in category['children']:
        title = i.get('name')
        sub_cate = dict()
        index = 1
        for j in i['children']:
            sub_cate[index] = j.get('name')
            index += 1

        cate_dict[title] = sub_cate

    return cate_dict


def get_trend_search():
    titles_list = []
    trendpost = []
    trending_df = pytrend.trending_searches(pn='vietnam')
    trend_table = trending_df.reset_index().to_json(orient='records')
    trend_data = []
    trend_data = json.loads(trend_table)

    for item in trend_data:
        item['index'] = item['index'] + 1
        item['name'] = item['0']
        del item['0']

    for item in trend_data:
        title = item.get('name')
        titles_list.append(title)

    for title in titles_list:
        r = ggl(title, lang='vi', max_results=5)
        for item in r:
            trend_dict = {
                'trend_name': title,
                'title': item.get('title').replace('...', ''),
                'link': item.get('href'),
                'body': item.get('body')
            }

            trendpost.append(trend_dict)

    return trendpost


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def get_ggt_data_from_api():
    url = GGT_API_1
    payload = {}
    headers = {
        'Cookie': 'NID=511=Aea-tt-tudrnRfSJZcPkQ2r157nErI7PkmNc_NpHqy-PUksT2N6lOlInuv5_TBwTl-YMuVP7FiCPXqWangEoYSO3MALwZWpFKfL-FIqtiB76XWv6k0nbLJlyzFr3-n_nF-xvUlZL3JMmxptb2OSSHjeMDd1nxyyRI4p18g_snq0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    json_data = (response.text).replace(")]}',", '')
    data = json.loads(json_data)
    results = list()
    for item in data['default']['trendingSearches']:
        data_dict = {
            'title': item['title'],
            'views': item['formattedTraffic'],
            'url': 'https://trends.google.com' + item['trendingSearchUrl'],
            'country': item['country'],
        }
        results.append(data_dict)
    return results


def get_ggt_full_data_from_api():
    url = GGT_API_2
    payload = {}
    headers = {
        'Cookie': 'NID=511=Aea-tt-tudrnRfSJZcPkQ2r157nErI7PkmNc_NpHqy-PUksT2N6lOlInuv5_TBwTl-YMuVP7FiCPXqWangEoYSO3MALwZWpFKfL-FIqtiB76XWv6k0nbLJlyzFr3-n_nF-xvUlZL3JMmxptb2OSSHjeMDd1nxyyRI4p18g_snq0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = (response.text).replace(")]}',", '')
    data = json.loads(json_data)
    results = list()
    for item in data['default']['trendingSearchesDays']:
        group_dict = dict()
        group_dict[item['formattedDate']] = item['trendingSearches']
        results.append(group_dict)

    return results


def get_related_keywords(text):
    url = f"https://www.google.com/complete/search?q={text}&cp=0&client=gws-wiz&xssi=t&hl=en-VN&authuser=0&psi=ArB8YpD_G7XNmAXFq4j4AQ.1652338691992&pq=14000000 byte = gb&ofp=null&nolsbt=1&dpr=1.25"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = (response.text).replace(")]}'", '')
    data = json.loads(json_data)
    # print(data)
    results = list()
    for item in data[0]:
        for i in item:
            i = html.unescape(remove_tags(i))
            results.append(i)
            break

    return results
