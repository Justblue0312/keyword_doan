from django.urls import path
from . import views


urlpatterns = [
    path('vnexpress/', views.getNewsPosts, name='vnexpress'),
]
