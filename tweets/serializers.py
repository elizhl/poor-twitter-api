from rest_framework import serializers
from .models import *

class TweetHyperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ('url', 'id', 'name', 'date', 'tweet',)