"""tweet a text and an image"""
import os
import shutil
from pathlib import Path

import requests
import tweepy

import config
from message import create_message_top_games, create_message_trending_games
from scrape import get_games

auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweet(message, images, debug=False):
    """Tweet a message and some image."""
    filenames = []
    folder = './assets/'
    dir_path = Path(folder)
    try:
        shutil.rmtree(dir_path)
        os.mkdir(folder)
    except OSError as error:
        print(f'Failed to delete {folder}. Reason: {error}')

    for i, image in enumerate(images):
        req = requests.get(image, allow_redirects=True)
        filename = f'{folder}tmp{str(i + 1)}.png'
        filenames.append(filename)
        with open(filename, 'wb') as file:
            file.write(req.content)

    if not debug:
        media_ids = []
        for filename in filenames:
            res = api.media_upload(filename)
            media_ids.append(res.media_id)
        print(len(message))
        api.update_status(media_ids=media_ids, status=message)
    print(f'Tweeted: {message}')


def init_tweet_trending():
    """initiate tweet"""
    games = get_games(True)
    images = [item[1]['image'] for item in games.items()]
    images = images[:3]
    images.append(
        'https://github.com/icepick4/daily-steam-stats/blob/'
        '77a358d594c053e491c7a26a76d6ff1e5611165b/steam-logo.png?raw=true')
    message = create_message_trending_games(games)
    tweet(message, images)


def init_tweet_top():
    """initiate tweet"""
    games = get_games(False)
    images = [item[1]['image'] for item in games.items()]
    images = images[:4]
    message = create_message_top_games(games)
    tweet(message, images)
