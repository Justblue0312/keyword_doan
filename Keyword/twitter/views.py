from django.http import HttpResponse
from django.shortcuts import render
from .utils import (getVietNamTwitterTrends, getWorldwideTwitterTrend,
                    getOthereTrendList)
from .models import (VietNamTwitterTrend, WorldwideTwitterTrend,
                     TopHashtagTrend, LongestTrend)


def getVietNamTwitterTrend(request):
    # VietNamTwitterTrend.objects.all().delete()
    # WorldwideTwitterTrend.objects.all().delete()
    TopHashtagTrend.objects.all().delete()
    LongestTrend.objects.all().delete()

    # vn_trends = getVietNamTwitterTrends(request)
    # for trend in vn_trends:
    #     m1 = VietNamTwitterTrend(**trend)
    #     m1.save()

    # ww_trends = getWorldwideTwitterTrend(request)
    # for trend in ww_trends:
    #     m2 = WorldwideTwitterTrend(**trend)
    #     m2.save()

    top_hashtag_list, longest_list = getOthereTrendList(request)
    for trend in top_hashtag_list:
        m3 = TopHashtagTrend(**trend)
        m3.save()

    for trend in longest_list:
        m4 = LongestTrend(**trend)
        m4.save()

    vn_trend_obj = VietNamTwitterTrend.objects.all()
    ww_trend_obj = WorldwideTwitterTrend.objects.all()
    top_hashtag_obj = TopHashtagTrend.objects.all()
    longest_obj = LongestTrend.objects.all()

    context = {'vn_trends': vn_trend_obj, 'ww_trends': ww_trend_obj,
               'top_trends': top_hashtag_obj, 'longest_trend': longest_obj}
    return render(request, 'twitter/tweet.html', context)
