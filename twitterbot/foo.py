import os
import json
import requests

def get_user_from_hashtag(mentions):
    """
    Function: 
        Checks the API for the latest #TweetToTwin hashtag.
    Arguments:
        Mentions of the user.
    Returns:
        A dict, with the user's id as the key and the last 50 hashtags
        posted by that user for each value.
    """
    hashtags = []
    for u in user while hashtags.size() < 50:
        hashtags.add(u['hashtags'])
    tweeter_dict = {user['id'] : hashtags}
        return tweeter_dict

def get_followers_of_user(tweeter_dict):
    """
    Function: 
        Checks the last 50 hashtags of each user and adds to a new dictionary.
    Arguments:
        tweeter_dict (dictionary):
        The dictionary of the original twitter's id and their associated most
        recent 50 hashtags.
    Returns:
        A new dict, with each key containing each follower's id and each value
        containing the last 50 hashtags posted by that user.
    """
    hashtags = []
    for f in follower while hashtags.size() < 50:
        hashtags.add(f['hashtags'])
    follower_dict = {follower['id'] : hashtags}
        return follower_dict

def find_similar_hashtags(follower_dict, tweeter_dict):
    """
    Function: 
        Iterates over each dictionary and searches for similar hashtags (values)
        between users.
    Arguments:
        tweeter_dict (dictionary):
        The dictionary of the original twitter's id and their associated most
        recent 50 hashtags.

        follower_dict (dictionary):
        The dictionary of each follower's id and their associated most recent
        50 hashtags.
    Returns:
        A string containing the id of the original user's "twin".
    """
    twin = str(max(hash_of_ints))
        return twin

def tweet_to_twin(twin, tweeter_dict):
    """
    Function: 
        Returns the id of the user's twin back to the original user.
    Arguments:
        tweeter_dict (dictionary):
        The dictionary of the original twitter's id and their associated most
        recent 50 hashtags.

        twin (string):
        A string containing the user's id.
    Returns:
        A tweet to the original user.
    """
        return "Your twin is" + twin + "!!!"

def latest_twin_tweet(tweets):
    """
    Given a list of tweets, finds the latest #TweetToTwin tweet.
    Arguments:
        tweets (list): a list of Twitter tweet objects that are dicts
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    for tweet in tweets:
        tags = [tag for tag in tweet['entities']['hashtags'] if tag['text'].contains('Your twin is')]
        if len(tags) > 0:
            return tweet
