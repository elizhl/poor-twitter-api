from django.db import models

# Create your models here.

class Tweet(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    tweet = models.CharField(max_length=50, blank=True, null=True)
