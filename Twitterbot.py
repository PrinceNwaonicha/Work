import tweepy
import time

API_KEY = "Custom_key"
API_SECRET = "Custom_key"
ACCESS_TOKEN = "Custom_key"
ACCESS_SECRET = "Custom_key"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        print("All Done!")
    except tweepy.TweepError:
        print("All Done!")


search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


 # Generous Bot
 # for follower in tweepy.Cursor(api.followers).items():
 #     follower.follow()
