from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Tweets
from api.messages import MESSAGE, CREATE_TWEET, DATA
from api.serializers import TweetSerializer, GetTweetSerializer


class TweetView(APIView):
    """
    Create tweet.
    """

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_data = {MESSAGE: CREATE_TWEET}
            return Response(response_data, status.HTTP_201_CREATED)

    #  Featch all tweets.
    def get(self, request):
        tweets = Tweets.objects.order_by("-created_at", "name")
        serializer = GetTweetSerializer(tweets, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
