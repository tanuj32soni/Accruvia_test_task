from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Tweets


class TweetSerializer(serializers.ModelSerializer):
    """
    Serializer for validate name and tweet fields and create tweets.
    """

    def create(self, data):
        instance = super().create(data)
        return instance

    class Meta:
        model = Tweets
        exclude = ("created_at",)


class GetTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = "__all__"
