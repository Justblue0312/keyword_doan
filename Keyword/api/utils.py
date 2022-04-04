import json
from pytrends.request import TrendReq
import urllib.parse
from ggtrends.utils import find_between

pytrend = TrendReq()


def trendSearchData(request):
    trending_df = pytrend.trending_searches(pn='vietnam')
    trend_table = trending_df.reset_index().to_json(orient='records')
    trend_data = []
    trend_data = json.loads(trend_table)

    for item in trend_data:
        item['index'] = item['index'] + 1
        item['key'] = item['0']
        del item['0']

    return trend_data


def todayTrendData(request):
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
