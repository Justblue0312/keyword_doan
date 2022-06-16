from django.contrib import admin
from .models import YearTrend, TodayTrends, TrendPosts, TrendHotPosts

admin.site.register(YearTrend)
admin.site.register(TodayTrends)
admin.site.register(TrendPosts)
admin.site.register(TrendHotPosts)
