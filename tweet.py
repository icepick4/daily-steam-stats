"""tweet a text and an image"""

import os
import shutil
import sys
from pathlib import Path

import requests
import tweepy

from constants import IDEAS_MESSAGE

try:
    import config
except ImportError:
    print('Please create a config.py file with your Twitter API keys.')
    sys.exit()
from message import (create_links_message, create_message_peak_of_the_day,
                     create_message_top_games, create_message_trending_games,
                     create_reply_message, cut_message)
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
        message[0] : main message (tab)
        message[1] : links to games (tab)
        message[2] : reply message (tab)
    """
    filenames = download_images(images)
    if not debug:
        media_ids = []
        for filename in filenames:
            # upload images
            res = api.media_upload(filename)
            media_ids.append(res.media_id)
        response = api.update_status(
            media_ids=media_ids, status=messages[0][0])
        print(f'Tweeting: {messages[0][0]}')
        if isinstance(messages[0], list):
            messages[0].pop(0)
        else:
            messages.pop(0)
        api.create_favorite(response.id)
    # for each message category, browse all the messages (they are already cut)
    for message in messages:
        for msg in message:
            # check if its the last message
            if msg == message[-1] and message == messages[-1]:
                msg = msg[:len(msg) - 2]
                if len(msg) + len(IDEAS_MESSAGE) < 275:
                    msg += IDEAS_MESSAGE
            print(f'Tweeting: {msg}\n')
            if not debug:
                response = api.update_status(
                    status=msg, in_reply_to_status_id=response.id)
                api.create_favorite(response.id)


def init_tweet_trending(debug):
    """initiate tweet"""
    games = get_games(True)
    if games is None:
        return
    message = create_message_trending_games(games)
    global_init(games, message, 'trending', debug)


def init_tweet_peak(debug):
    """initiate tweet"""
    games = get_games(False)
    if games is None:
        return
    message = create_message_peak_of_the_day(games)
    # sort games by peak
    games = sorted(
        games.items(), key=lambda x: x[1]['peak_players'], reverse=True)
    games = dict(games)
    global_init(games, message, 'peak', debug)


def init_tweet_top(debug):
    """initiate tweet"""
    games = get_games(False)
    if games is None:
        return
    message = create_message_top_games(games)
    global_init(games, message, 'top', debug)


def global_init(games, message, type, debug):
    """initiate tweet"""
    images = [item[1]['image'] for item in games.items()]
    images = images[:4]
    main_message = message[0]
    links = [item[1]['steam_link'] for item in games.items()]
    links = create_links_message(links, message[1])
    reply = create_reply_message(message[1], type)[0]
    tweet([cut_message(main_message), cut_message(
        links), cut_message(reply)], images, debug)


def download_images(images):
    """download images"""
    filenames = []
    folder = './assets/'
    try:
        shutil.rmtree(Path(folder))
        os.mkdir(folder)
    except OSError as error:
        print(f'Failed to delete {folder}. Reason: {error}')
        print('Create a folder named "assets" in the root directory.')
        sys.exit()

    for i, image in enumerate(images):
        req = requests.get(image, allow_redirects=True, timeout=15)
        filename = f'{folder}tmp{str(i + 1)}.png'
        filenames.append(filename)
        try:
            with open(filename, 'wb') as file:
                file.write(req.content)
        except FileNotFoundError:
            print('Create a folder named "assets" in the root directory.')
            sys.exit()
    return filenames
