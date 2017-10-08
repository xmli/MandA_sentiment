from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob


#consumer key, consumer secret, access token, access secret.
consumer_key = 'S2nnlvMfjKw6AB6JzZxPQU305'
consumer_secret = '1H0btag79ui1pJTkhDIzldWNhVaQkjWRPVpsH0pTt6oUPA2ftR'
access_token = '575946480-FyvKX1pzDjXDhYximlCcHFddYAlVs5Jrw8hzfAqv'
access_token_secret = '7ixwwMFMminLsYZmT1iaZD7zn17a7BSZrAREwOsr9Y4xE'

query = str(input("What do you want to query about? \n>"))
print("Tracking " + query + "...")

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']

        analysis = TextBlob(tweet)
        polarity = analysis.sentiment[0]
        subjectivity = analysis.sentiment[1]

        # print(tweet, polarity, subjectivity)
        print(tweet)

        output = open('twitter_output.txt', 'a')
        if polarity > 0.05:
            output.write('pos')
        elif polarity < -0.05:
            output.write('neg')
        output.write('\n')
        output.close()

        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=[query])