from rest_framework import serializers
from ggtrends.models import YearTrend, TodayTrends, TrendPosts
from facebook.models import Post
from twitter.models import LongestTrend, TopHashtagTrend, VietNamTwitterTrend, WorldwideTwitterTrend
from vnexpress.models import NewsPost


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'


class LongestTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongestTrend
        fields = '__all__'


class TopHashtagTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopHashtagTrend
        fields = '__all__'


class WorldwideTwitterTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldwideTwitterTrend
        fields = '__all__'


class VietNamTwitterTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = VietNamTwitterTrend
        fields = '__all__'


class FbPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TrendKeywordSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    key = serializers.CharField()


class TrendSearchSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    exploreLink = serializers.CharField()


class YearTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearTrend
        fields = '__all__'


class TodayTrendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayTrends
        fields = '__all__'


class TrendPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendPosts
        fields = '__all__'
