from django.urls import path
from . import views

urlpatterns = [
    path('trends_home/', views.trends_home, name='trends_home'),
    path('ggtrends/', views.trend_index, name='trend_index'),
    path('search/', views.search, name='search'),

    path(r'trendpost/<str:trendname>/',
         views.get_trendpost_by_trend, name='trendpost'),
    path(r'hotpost/<str:trendname>/',
         views.get_hotpost, name='hotpost')

]
