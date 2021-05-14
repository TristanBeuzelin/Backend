from django.db import models

# Create your models here.

class Tweet(models.Model):
    tweet = models.CharField(max_length=280, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    username = models.CharField(max_length=100, null=False, blank=False, default='Joe_the_default_guy')

    def __str__(self):
        return self.tweet
