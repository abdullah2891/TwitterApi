import json
import pandas as pd
import matplotlib.pyplot as plt


__author__ = 'Abdullah_Rahman'

file = 'data.json'
tweets_data =[]
tweets_file = open(file,'r')
lang = []
for line in tweets_file:
    try:
        tweet =json.loads(line)
        lang.append(tweet["retweeted_status"])
        tweets_data.append(tweet)
    except:
        continue


print len(tweets_data)

for l in lang:
    print l["user"]["location"]
