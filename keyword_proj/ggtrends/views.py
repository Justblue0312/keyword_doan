from django.shortcuts import render

from others.models import Keyword
from news.models import ArticleNews
from facebook.models import Post
from .utils import *
import pandas as pd
import json
import datetime
from google_searching import ggl
from .models import YearTrend, TodayTrends, TrendPosts, TrendHotPosts
from pytrends.request import TrendReq
from django.db.models import Q

pytrends = TrendReq()


def trends_home(request):
    titles_list = todayTrendList(request)

    TodayTrends.objects.all().delete()
    TrendPosts.objects.all().delete()
    for title in titles_list:
        todaytrend_obj = TodayTrends(trend_name=title)
        todaytrend_obj.save()
        req = ggl(title, lang='vi', max_results=3)
        for item in req:
            trendpost_obj = TrendPosts(
                trend_name=TodayTrends.objects.get(trend_name=title),
                title=item.get('title').replace('...', ''),
                link=item.get('href'),
                body=item.get('body'),
            )
            trendpost_obj.save()

    todaytrend_Obj = TodayTrends.objects.all()
    trendpost_Obj = TrendPosts.objects.all()

    context = {'todaytrends': todaytrend_Obj,
               'trendposts': trendpost_Obj}

    return render(request, 'ggtrends/trends_home.html', context)


def trend_index(request):
    date = datetime.date.today()
    year = date.strftime("%Y")

    trend_data = trendSearch(request)

    today_trend = todayTrend(request)

    fy_trend = getTheLastFiveYearsTrend(request, int(year))

    year_trends = getTheLastFiveYearsTrendDict(request, int(year))

    YearTrend.objects.all().delete()
    for year_trend in year_trends:
        yt_model = YearTrend(**year_trend)
        yt_model.save()

    cate_trend = trendCategories(request)

    context = {'trend_data': trend_data,
               'today_trend': today_trend, 'fy_trend': fy_trend, 'cate_trend': cate_trend}

    return render(request, 'ggtrends/hot_search.html', context=context)


def search(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        keyword = pytrends.suggestions(search_query)

        df = pd.DataFrame(keyword)
        keytable = df.reset_index().to_json(orient='records')
        suggestions = []
        suggestions = json.loads(keytable)

        for item in suggestions:
            item['index'] = item['index'] + 1

        keyword_obj = Keyword.objects.filter(
            Q(keyword__startswith=search_query) |
            Q(keyword__icontains=search_query)
        )

        keyword = [i for i in keyword_obj]
        # print(keyword)

        posts = Post.objects.filter(
            Q(content__icontains=search_query)
        )

        news = ArticleNews.objects.filter(
            Q(title__icontains=search_query) |
            Q(abstract__icontains=search_query) |
            Q(content__icontains=search_query)
        )

        context = {'search_query': search_query,
                   'suggestions': suggestions,
                   'keyword': keyword,
                   'posts': posts,
                   'news': news}
        return render(request, 'ggtrends/search.html', context)
    else:
        context = {}
        return render(request, 'ggtrends/search.html', context)


def get_trendpost_by_trend(request, trendname):
    trendpost_obj = TrendPosts.objects.filter(
        trend_name=TodayTrends.objects.get(trend_name=trendname))
    context = {
        'trendpost': trendpost_obj
    }
    return render(
        request,
        'ggtrends/trendposts.html',
        context
    )


def get_hotpost(request, trendname):
    trendpost_obj = TrendHotPosts.objects.filter(trend_name=trendname)
    context = {
        'trendpost': trendpost_obj
    }
    return render(
        request,
        'ggtrends/trendposts.html',
        context
    )
