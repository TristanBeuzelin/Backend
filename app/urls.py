from django.urls import path
from . import views

urlpatterns = [
    path('lasttweets', views.TweetListCreate.as_view()),
    path('tweet', views.TweetSave),
    path('', views.index),
]