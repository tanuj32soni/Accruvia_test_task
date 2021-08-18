from django.db import models


class Tweets(models.Model):
    """
    Store user tweets.
    """

    name = models.CharField(max_length=30)
    tweet = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_tweets"

    def __str__(self):
        return "{}".format(self.name)
