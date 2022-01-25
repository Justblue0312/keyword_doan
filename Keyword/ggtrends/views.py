from django.shortcuts import render
from .utils import trendSearch, searchWords, searchStat


def home(request):
    return render(request, 'home.html')


def index(request):
    trend_data = trendSearch(request)
    # suggestions, search_query = searchWords(request)
    # interest = searchStat(request)

    context = {'trend_data': trend_data}

    return render(request, 'ggtrends/hot_search.html', context=context)
