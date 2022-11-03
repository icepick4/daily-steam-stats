"""create a message for a tweet"""
import random

import pyshorteners

from constants import (CHART_INCREASING, DOWN_ARROW, END_MESSAGE, GLOB,
                       HASHTAGS, NUMBERS, PERSON, REPLY_MESSAGE_PEAK,
                       REPLY_MESSAGE_TOP, REPLY_MESSAGE_TRENDING, RIGHT_ARROW,
                       SHOPPING_CART, TROPHY, VIDEO_GAME)


def create_message_top_games(games):
    """Create a message for a tweet."""
    message = f'Top 10 most played #games on #Steam currently {TROPHY}{GLOB}\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        games_names.append(item[0])
        current_players = item[1]['current_players']
        message += ((f'{rank}-{item[0]} (Currently : {current_players} {PERSON})\n'))
        # add a hashtag for each game (without spaces and special characters)
        message += '#' + ''.join(e for e in item[0] if e.isalnum()) + '\n'
    return add_hashtags(message, games_names)


def create_message_peak_of_the_day(games):
    """Create a message for a tweet."""
    message = f'Peak players today on #Steam !{GLOB}{TROPHY}\n\n'
    games_names = []
    sorted_games = sorted(
        games.items(), key=lambda x: x[1]['peak_players'], reverse=True)
    sorted_games = dict(sorted_games)
    for i, item in enumerate(sorted_games.items()):
        rank = get_rank(i+1)
        games_names.append(item[0])
        peak_players = item[1]['peak_players']
        message += (
            (f'{rank} {item[0]} (Peak players: {peak_players} {PERSON})\n'))
        # add a hashtag for each game (without spaces and special characters)
        message += '#' + ''.join(e for e in item[0] if e.isalnum()) + '\n'
    return add_hashtags(message, games_names)


def create_message_trending_games(games):
    """Create a message for a tweet."""
    message = f'Top 5 trending #games on #Steam currently {TROPHY}\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        evolution = item[1]['evolution']
        games_names.append(item[0])
        message += (
            (f'{rank} {item[0]} (Last 24 hours : {evolution} {CHART_INCREASING})\n'))
        # add a hashtag for each game (without spaces and special characters)
        message += '#' + ''.join(e for e in item[0] if e.isalnum()) + '\n'
    return add_hashtags(message, games_names)


def create_reply_message(games, tweet_type):
    """Create a reply message for a tweet."""
    if tweet_type == "trending":
        return add_hashtags(REPLY_MESSAGE_TRENDING, games)
    if tweet_type == "peak":
        return add_hashtags(REPLY_MESSAGE_PEAK, games)
    return add_hashtags(REPLY_MESSAGE_TOP, games)


def create_links_message(links, games):
    """Create a message to display links of games"""
    message = f'Links of the #games in the #leaderboard #today {TROPHY}{VIDEO_GAME}\n\n'
    for i, link in enumerate(links):
        link = pyshorteners.Shortener().tinyurl.short(link)
        line = f'{games[i]} {RIGHT_ARROW} {link} {SHOPPING_CART}\n'
        message += line
    message += '\n'
    message += END_MESSAGE
    return message


def add_hashtags(message, games):
    """add hashtags to the message"""
    message += '\n'
    hashtag = ''
    for i in range(1, 7):
        while hashtag in message:
            hashtag = random.choice(HASHTAGS)
        message += f'{hashtag} '
        if i % 2 == 0:
            message += '\n'
    message += '\n' + END_MESSAGE
    # return the main message and the games names
    return message, games


def get_rank(rank):
    """getting the rank of the game in emojis"""
    if rank == 1:
        rank = "\U0001F947"
    elif rank == 2:
        rank = "\U0001F948"
    elif rank == 3:
        rank = "\U0001F949"
    else:
        rank = NUMBERS[rank]
    return rank


def cut_message(message):
    """cut the message into many messages with 280 characters"""
    messages = message.split('\n')
    final_messages = []
    while messages != []:
        message = ''
        # cut messages into 280 characters messages
        while len(message) + len(messages[0]) < 265:
            message += messages[0] + '\n'
            messages.pop(0)
            if messages == []:
                break
        if message[-2] != '\n':
            message += '\n'
        message += DOWN_ARROW
        final_messages.append(message)
    # final messages contains messages cut into 280 characters
    return final_messages
