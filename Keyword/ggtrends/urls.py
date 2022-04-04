from django.urls import path
from . import views

urlpatterns = [
    path('ggtrends/', views.index, name='index'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
]
