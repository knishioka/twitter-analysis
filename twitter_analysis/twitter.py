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


def friends_ids(id):
    """Get all friend ids.

    Args:
        id (str): either screen name or user id.

    Returns:
        `set` of `int`: user id list.

    """
    return [friend for friend in tweepy.Cursor(twitter_api().friends_ids, id).items()]


def followers_ids(id):
    """Get all follower ids.

    Args:
        id (str): either screen name or user id.

    Returns:
        `set` of `int`: user id list.

    """
    return [follower for follower in tweepy.Cursor(twitter_api().followers_ids, id).items()]


def friends_intersection(*ids):
    """Get friends intersection.

    Args:
        id1 (str): either screen name or user id.
        id2 (str): either screen name or user id.

    Returns:
        `list` of `int`: user id list.

    """
    return set.intersection(*[set(friends_ids(target_id)) for target_id in ids])


def followers_intersection(*ids):
    """Get followers intersection.

    Args:
        id1 (str): either screen name or user id.
        id2 (str): either screen name or user id.

    Returns:
        `list` of `int`: user id list.

    """
    return set.intersection(*[set(followers_ids(target_id)) for target_id in ids])
