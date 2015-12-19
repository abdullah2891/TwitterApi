from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



consumer_key=""
consumer_secret=""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""


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
