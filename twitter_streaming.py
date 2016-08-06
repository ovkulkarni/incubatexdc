import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "712421425257320448-t920gNKBHoxBhouq9RZItmPF8hRWTMX"
access_token_secret = "sDt9MlcSz7I3LtpCck4OvqUeRrZ1E0H5Bm7P8v9V0blNv"
consumer_key = "Ue0bHSCdd7DmF20LjTyoktxbI"
consumer_secret = "lHvpDnw7Zb9QhpVymPzqPgXacfQuJQ0ynAeVIFYACmvRJgrk4B"

tweets = []
urls = []
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'fcpsnews', count = 3, include_rts = True)

for status in stuff:
    #print status.text.encode('utf8')
    tweets.append(status.text.encode('utf8'))
    for url in status.entities['urls']:
         #print url['expanded_url']
         urls.append(url['expanded_url'])
print tweets
print urls
    