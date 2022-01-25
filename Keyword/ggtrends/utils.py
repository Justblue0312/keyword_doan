from keyword import kwlist
import re
from .models import GoogleWord
import pandas as pd
import json
from pytrends.request import TrendReq

pytrend = TrendReq()


def trendSearch(request):
    trending_df = pytrend.trending_searches(pn='vietnam')
    trend_table = trending_df.reset_index().to_json(orient='records')
    trend_data = []
    trend_data = json.loads(trend_table)

    return trend_data


def searchStat(request):
    trending_df = pytrend.trending_searches(pn='vietnam').to_dict('list')
    trend_list = list(trending_df.values())

    kw_list = []
    for trend in trend_list:
        if len(trend_list) < 5:
            kw_list.append(trend)

    pytrend.build_payload(kw_list=kw_list)
    interest_over_time_df = pytrend.interest_over_time()

    return interest_over_time_df


def searchWords(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    keyword = pytrend.suggestions(search_query)

    df = pd.DataFrame(keyword)
    keytable = df.reset_index().to_json(orient='records')
    suggestions = []
    suggestions = json.loads(keytable)

    return suggestions, search_query
