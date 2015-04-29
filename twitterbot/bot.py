import json
import os
import requests
import time
import "foo.py"
import "twit_utils.py"
CREDS_FILE = "~/Desktop/tw.json"

def make_it_so():
	# Step 1. Get my latest tweets.
	tweets = twit_utils.get_latest_tweets_from_me(CREDS_FILE)
    print("Found", len(tweets), "tweets")

	# Step 2. From my tweets, get the last time I sent a #TweetToTwin message.
	twinseeker = foo.latest_twin_tweet(tweets)
    if twinseeker:
        user_id = twinseeker['in_reply_to_status_id']
    else:
        user_id = 1
    print("Searching for mentions with an id later than", user_id)

	# Step 3: Get the most recent hashtag #TweetToTwin since my last reply.
	mentions = twit_utils.get_mentions(CREDS_FILE, {"since_id": xid})
    print("Found", len(mentions), "mentions")

	# Step 4: Keep that associated user's id and last 50 tweets in a dictionary.
	the_user = foo.get_user_from_hashtag(mentions)

	# Step 5: For each of that user's followers, take those users' ids and last 50
	# tweets.
	the_followers = foo.get_followers_of_user(this_user)

	# Step 6: Iterate through and find similar hashtags. Find the user's twin.
	twin = foo.find_similar_hashtags(the_followers, the_user)

	# Step 6: Create the custom tweet containing the twin.
	print("About to send a message to", the_user['user']['screen_name'])
    txt = foo.tweet_to_twin(twin, the_user)

	# Step 7: Send the message.
	 resp = twit_utils.reply(CREDS_FILE, txt, twinseeker)
       return resp

while True:
	make_it_so()
	time.sleep(10)