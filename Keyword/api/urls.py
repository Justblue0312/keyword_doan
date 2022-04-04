from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('trend_keywords/', views.TodayTrendsViews.as_view()),
    path('today_trends/', views.TrendsSearchViews.as_view()),

    path('trend_today/', views.getTodayTrends),
    path('trend_today/<str:pk>/', views.getTodayTrend),

    path('trend_post/', views.getTrendPosts),
    path('trend_post/<str:pk>/', views.getTrendPost),

    path('year_trends/', views.getYearTrends),
    path('year_trends/<int:year>/', views.getYearTrend),

    path('fb_posts/', views.getFacebookPosts),
    path('fb_posts/<str:pk>/', views.getFacebookPost),

    path('vntt_trends/', views.getVietNamTwitterTrends),
    path('vntt_trends/<str:pk>/', views.getVietNamTwitterTrend),

    path('ww_trends/', views.getWorldWideTwitterTrends),
    path('ww_trends/<str:pk>/', views.getWorldWideTwitterTrend),

    path('top_hashtag/', views.getTopHashtags),
    path('top_hashtag/<str:pk>/', views.getTopHashtag),

    path('longest_trends/', views.getLongestTrends),
    path('longest_trends/<str:pk>/', views.getLongestTrend),
]
