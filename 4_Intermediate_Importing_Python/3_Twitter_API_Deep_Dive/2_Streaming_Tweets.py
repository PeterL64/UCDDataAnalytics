# Streaming Tweets

# Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication by passing tweepy.Stream() the authentication handler: auth
# and the Stream listener: l.
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
# To filter Twitter streams, pass to the track argument in stream.filter() a list containing
# the desired keywords: 'clinton', 'trump', 'sanders', and 'cruz'
stream.filter(track=['clinton','trump','sanders','cruz'])


# Here is the sample Tweet Stream Listener Class (not expected to know how to write it at this stage):

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)
