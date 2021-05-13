from django.shortcuts import render
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework import generics

class TweetListCreate(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
