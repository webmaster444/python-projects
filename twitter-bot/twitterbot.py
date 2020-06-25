import tweepy
import time
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)

public_tweets = api.home_timeline()

user = api.me()  # info about me

for tweet in public_tweets:
    print(tweet.text)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == "Follower name":
        follower.follow()
        break

search_string = 'python'
numbersOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('i liked that one')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
