from __future__ import absolute_import, print_function
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="m7t8TcAZqZaDXuLiOACNvMDQ4"
consumer_secret="KW1DePIYu9FXwgRuqgisLfFcuXELEesN2GVAysqf4wMPFBkb8w"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="2768560599-AMsK5WwteYOBPX3Vc1Cvk9Oc9H3USu18kzRHZeA"
access_token_secret="VGGBQ1ZRNUvsKLGk9AnJ2BNAqDEnOdMgl0cTruMFVhlhz"



# If the authentication was successful, you should
# see the name of the account print out
class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, tweetFile):
        self.tweetFile = tweetFile

    def on_data(self, data):
	try:
            print(data)
	    with open(self.tweetFile, 'a') as tf:
                tf.write(data)
        except BaseException as s:
            print ("Error on_data: %s" % str(s))
        return True

    def on_error(self, status):
	print(status)

class StreamProcessor():
    def __init__(self):
        pass

    def stream_tweets(self, tweetFile, searchList):
        l = StdOutListener(tweetFile)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        stream = tweepy.Stream(auth=api.auth, listener = l)
        stream.filter(track=searchList)

if __name__ == '__main__':

    searchList = ["#marchmadness"]
    tweetFile = "tweets.json"

    streamer =StreamProcessor()
    streamer.stream_tweets(tweetFile, searchList)
