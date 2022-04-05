from rest_framework import views

from ggtrends.models import YearTrend, TodayTrends, TrendPosts
from .utils import trendSearchData, todayTrendData
from .serializers import (TrendKeywordSerializer, TrendSearchSerializer, YearTrendSerializer,
                          TodayTrendsSerializer, TrendPostsSerializer, FbPostSerializer,
                          VietNamTwitterTrendSerializer, WorldwideTwitterTrendSerializer,
                          TopHashtagTrendSerializer, LongestTrendSerializer, NewsPostSerializer)

from facebook.models import Post
from twitter.models import LongestTrend, TopHashtagTrend, VietNamTwitterTrend, WorldwideTwitterTrend
from vnexpress.models import NewsPost

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/today_trends/'},
        {'GET': '/api/trend_keywords/'},

        {'GET': '/api/year_trends/'},
        {'GET': '/api/year_trends/<int:year>/'},

        {'GET': '/api/trend_today/'},
        {'GET': '/api/trend_today/<str:pk>/'},

        {'GET': '/api/trend_post/'},
        {'GET': '/api/trend_post/<str:pk>/'},

        {'GET': '/api/fb_post/'},
        {'GET': '/api/fb_post/<str:pk>/'},

        {'GET': '/api/vntt_trends/'},
        {'GET': '/api/vntt_trends/<str:pk>/'},

        {'GET': '/api/ww_trends/'},
        {'GET': '/api/ww_trends/<str:pk>/'},

        {'GET': '/api/top_hashtag/'},
        {'GET': '/api/top_hashtag/<str:pk>/'},

        {'GET': '/api/longest_trends/'},
        {'GET': '/api/longest_trends/<str:pk>/'},

        {'GET': '/api/news_posts/'},
        {'GET': '/api/news_posts/<str:pk>/'},
    ]
    return Response(routes)


@api_view(['GET'])
def getNewsPosts(request):
    trends = NewsPost.objects.all()
    serializer = NewsPostSerializer(trends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNewsPost(request, pk):
    trends = NewsPost.objects.get(id=pk)
    serializer = NewsPostSerializer(trends, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getTopHashtags(request):
    trends = TopHashtagTrend.objects.all()
    serializer = TopHashtagTrendSerializer(trends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTopHashtag(request, pk):
    trends = TopHashtagTrend.objects.get(id=pk)
    serializer = TopHashtagTrendSerializer(trends, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getLongestTrends(request):
    trends = LongestTrend.objects.all()
    serializer = LongestTrendSerializer(trends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getLongestTrend(request, pk):
    trends = LongestTrend.objects.get(id=pk)
    serializer = LongestTrendSerializer(trends, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getWorldWideTwitterTrends(request):
    trends = WorldwideTwitterTrend.objects.all()
    serializer = WorldwideTwitterTrendSerializer(trends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getWorldWideTwitterTrend(request, pk):
    trends = WorldwideTwitterTrend.objects.get(id=pk)
    serializer = WorldwideTwitterTrendSerializer(trends, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getVietNamTwitterTrends(request):
    trends = VietNamTwitterTrend.objects.all()
    serializer = VietNamTwitterTrendSerializer(trends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVietNamTwitterTrend(request, pk):
    trends = VietNamTwitterTrend.objects.get(id=pk)
    serializer = VietNamTwitterTrendSerializer(trends, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getFacebookPosts(request):
    fbpost = Post.objects.all()
    serializer = FbPostSerializer(fbpost, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFacebookPost(request, pk):
    fbpost = Post.objects.get(id=pk)
    serializer = FbPostSerializer(fbpost, many=False)
    return Response(serializer.data)


class TodayTrendsViews(views.APIView):

    def get(self, request):
        trend_search = trendSearchData(request)
        results = TrendKeywordSerializer(trend_search, many=True).data
        return Response(results)


class TrendsSearchViews(views.APIView):

    def get(self, request):
        today_search = todayTrendData(request)
        results = TrendSearchSerializer(today_search, many=True).data
        return Response(results)


@api_view(['GET'])
def getYearTrends(request):
    yearTrends = YearTrend.objects.all()
    serializer = YearTrendSerializer(yearTrends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getYearTrend(request, year):
    yearTrend = YearTrend.objects.get(year_trend=year)
    serializer = YearTrendSerializer(yearTrend, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getTodayTrends(request):
    today_trends = TodayTrends.objects.all()
    serializer = TodayTrendsSerializer(today_trends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTodayTrend(request, pk):
    today_trend = TodayTrends.objects.get(id=pk)
    serializer = TodayTrendsSerializer(today_trend, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getTrendPosts(request):
    trendposts = TrendPosts.objects.all()
    serializer = TrendPostsSerializer(trendposts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTrendPost(request, pk):
    trendpost = TrendPosts.objects.get(id=pk)
    serializer = TrendPostsSerializer(trendpost, many=True)
    return Response(serializer.data)
