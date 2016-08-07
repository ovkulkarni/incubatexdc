from __future__ import print_function

import os
from nude import Nude

import tweepy
import os
import requests
import wget

#Variables that contains the user credentials to access Twitter API 
access_token = os.getenv("TWITTER_ACCESS_TOKEN", "712421425257320448-t920gNKBHoxBhouq9RZItmPF8hRWTMX")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET", "sDt9MlcSz7I3LtpCck4OvqUeRrZ1E0H5Bm7P8v9V0blNv")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY", "Ue0bHSCdd7DmF20LjTyoktxbI")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET", "lHvpDnw7Zb9QhpVymPzqPgXacfQuJQ0ynAeVIFYACmvRJgrk4B")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

timeline = api.user_timeline(screen_name= "markchangdc")

media_files = set()
for status in timeline:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
for media_file in media_files:
   filename = wget.download(media_file);
   n = Nude(os.path.join(str(filename)))
   n.parse()
   print(n.result, n.inspect())
   print(media_file);
   

