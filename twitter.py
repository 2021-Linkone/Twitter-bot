import tweepy
import settings

CONSUMER_KEY = settings.CONSUMER_KEY
CONSUMER_SECRET = settings.CONSUMER_SECRET
ACCESS_TOKEN = settings.ACCESS_TOKEN
ACCESS_SECRET = settings.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

search_results = api.search(q="大学", count=100)

for result in search_results:
    tweet_id = result.id
    user_id = result.user._json['id']  
    try:
        api.create_favorite(tweet_id) #いいね
        api.retweet(tweet_id)          #リツイート
        api.create_friendship(user_id)  #フォロー
    except Exception as e:
        print(e)