from django.shortcuts import render
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from datetime import datetime

class TweetListCreate(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

def TweetSave(request):
    print(request.POST)
    tweet = Tweet.objects.create(tweet=request.POST.get('tweet'), date=datetime.now(), username=request.POST.get('username'))
    tweet.save()
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')