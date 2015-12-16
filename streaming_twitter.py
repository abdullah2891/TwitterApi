from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



consumer_key="8i012pQfHOX3XDHz3surESXlz"
consumer_secret="HckTjwCVdgfP5OKtFhAcAD4rY9fZgqMHIxVY5HuLXGFg2j6fm5"
ACCESS_TOKEN = "135724869-aaQkFJRNaS5Oo9nHRrABbL9PBw5osPhfRjJcbwdC"
ACCESS_SECRET = "9iVEFq9WKx1NpcYYGs1P4Qq1zoX4zVQ5pgAY1KnfpPWad"


class StdOutListener(StreamListener):
    def on_data(self,data):
        print data
        return True

    def on_error(self,status):
        print status



if __name__=='__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    stream = Stream(auth,l)
    #this line filters python javascript ruby
    stream.filter(track=['python','javascript','ruby'])
