from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from tweets.views import *

router = DefaultRouter()
router.register(r'tweet', TweetViewSet, 'tweet')

urlpatterns = [
    path('', include(router.urls)),
]
