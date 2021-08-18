from django.urls import path
from api import views

urlpatterns = [
    path("tweet/", views.TweetView.as_view(), name="tweet"),
]
