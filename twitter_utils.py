import tweepy
import os
import wget
from textutils import analyze
from nude import is_nude

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
		try:
			analysis[tweet.id] = analyze(tweet.text)

		except:
			media_files = tweet.entities.get("media", [])
			analysis[tweet.id] = "none"
			for file in media_files:
				filename = wget.download(file["media_url"])
				if is_nude(str(filename)):
					analysis[tweet.id] = "bad"
					break
			os.system('rm *.jpg')
	return analysis