import json

tweetFile = './tweets.json'

data = []
with open(tweetFile, 'r') as tf:
    for line in tf:
        try:
            tweet = json.loads(line)
            data.append(tweet)
        except:
            continue
print len(data)
