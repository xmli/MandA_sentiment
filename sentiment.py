import tweepy
from textblob import TextBlob

consumer_key = 'S2nnlvMfjKw6AB6JzZxPQU305'
consumer_secret = '1H0btag79ui1pJTkhDIzldWNhVaQkjWRPVpsH0pTt6oUPA2ftR'
access_token = '575946480-FyvKX1pzDjXDhYximlCcHFddYAlVs5Jrw8hzfAqv'
access_token_secret = '7ixwwMFMminLsYZmT1iaZD7zn17a7BSZrAREwOsr9Y4xE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('$AAPL')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)