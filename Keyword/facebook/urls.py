from django.urls import path
from . import views

urlpatterns = [
    path('facebook/', views.getPosts, name='facebook')
]
