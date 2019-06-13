from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetHyperSerializer

    def perform_create(self, serializer):
        obj = serializer.save()

    def get_queryset(self):
        return Tweet.objects.all()
