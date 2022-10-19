"""tweet a text and an image"""
import os
import shutil
import sys
from pathlib import Path

import requests
import tweepy

try:
    import config
except ImportError:
    print('Please create a config.py file with your Twitter API keys.')
    sys.exit()
from constants import LOGO_IMAGE
from message import (create_links_message, create_message_top_games,
                     create_message_trending_games, create_reply_message)
from scrape import get_games

try:
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
except tweepy.TweepyException:
    print('Failed to authenticate with Twitter.')
    sys.exit()


def tweet(messages, images, debug=False):
    """Tweet a message and some image.
        message[0] : main message
        message[1] : links to games
        message[2] : reply message
    """
    filenames = []
    folder = './assets/'
    try:
        shutil.rmtree(Path(folder))
        os.mkdir(folder)
    except OSError as error:
        print(f'Failed to delete {folder}. Reason: {error}')

    for i, image in enumerate(images):
        req = requests.get(image, allow_redirects=True, timeout=1)
        filename = f'{folder}tmp{str(i + 1)}.png'
        filenames.append(filename)
        with open(filename, 'wb') as file:
            file.write(req.content)

    if not debug:
        media_ids = []
        for filename in filenames:
            res = api.media_upload(filename)
            media_ids.append(res.media_id)
        reponse = api.update_status(media_ids=media_ids, status=messages[0])
        api.create_favorite(reponse.id)
        reponse = api.update_status(in_reply_to_status_id=reponse.id,
                                    status=messages[1])
        api.create_favorite(reponse.id)
        reponse = api.update_status(in_reply_to_status_id=reponse.id,
                                    status=messages[2])
        api.create_favorite(reponse.id)
    print(f'Tweeted: {messages[0]}\n')
    print(f'Replied: {messages[1]}\n')
    print(f'Links: {messages[2]}')


def init_tweet_trending(debug):
    """initiate tweet"""
    games = get_games(True)
    images = [item[1]['image'] for item in games.items()]
    images = images[:3]
    images.append(LOGO_IMAGE)
    # message[0] : main message
    # message[1] : games names
    message = create_message_trending_games(games)
    main_message = message[0]
    links = [item[1]['steam_link'] for item in games.items()]
    # use the games names in message[1] to create reply message and links
    links = create_links_message(links, message[1])[0]
    reply = create_reply_message(message[1])[0]
    tweet([main_message, links, reply], images, debug)


def init_tweet_top(debug):
    """initiate tweet"""
    games = get_games(False)
    images = [item[1]['image'] for item in games.items()]
    images = images[:4]
    message = create_message_top_games(games)
    links = [item[1]['steam_link'] for item in games.items()]
    tweet([message[0], create_reply_message(message[1])[0], links], images, debug)
