import os

import tweepy


def twitter_api():
    """Create api client to access twitter API."""
    consumer_token = os.environ["CONSUMER_TOKEN"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_token = os.environ["ACCESS_TOKEN"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)
