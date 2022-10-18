"""main file"""
import tweepy

import config

client = tweepy.Client(access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET,
                       consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET
                       )
# Replace the text with whatever you want to Tweet about
# response = client.create_tweet(text='hello world')

# print(response)
