import tweepy
import os
from textutils import analyze

#Variables that contains the user credentials to access Twitter API 
access_token = os.getenv("TWITTER_ACCESS_TOKEN", "")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET", "")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY", "")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET", "")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(user="pokevisiongo"):
	return api.user_timeline(screen_name=user)

def analyze_tweets(tweets):
	analysis = {}
	for tweet in tweets:
		analysis[tweet.id] = analyze(tweet.text)
	return analysis
