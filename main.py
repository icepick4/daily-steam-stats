"""main file"""
import tweepy

import config
from message import create_message_trending_games
from scrape import get_games
from tweet import tweet

auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def main():
    """main function"""
    games = get_games(True)
    images = [item[1]['image'] for item in games.items()]
    images = images[:5]
    message = create_message_trending_games(games)
    tweet(message, images, api, True)


if __name__ == '__main__':
    main()
