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
                     create_message_trending_games, create_reply_message,
                     cut_message)
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
        # response = api.update_status(
        #     media_ids=media_ids, status=messages[0][0].pop(0))
        # api.create_favorite(response.id)
    for message in messages:
        for msg in message:
            print(f'Tweeting: {msg}')
            # response = api.update_status(
            #     status=msg, in_reply_to_status_id=response.id)
            # api.create_favorite(response.id)
    # cut_message(messages[0])
    # cut_message(messages[1])


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
    main_message = message[0]
    links = [item[1]['steam_link'] for item in games.items()]
    links = create_links_message(links, message[1])[0]
    reply = create_reply_message(message[1])[0]
    tweet([cut_message(main_message), cut_message(
        links), cut_message(reply)], images, debug)
