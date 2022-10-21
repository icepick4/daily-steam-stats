"""create a message for a tweet"""
import random

import pyshorteners

from constants import (ARROW, CHART_INCREASING, NUMBERS, REPLY_MESSAGE_TOP,
                       REPLY_MESSAGE_TRENDING, TROPHY, hashtags)


def create_message_top_games(games):
    """Create a message for a tweet."""
    message = f'Top 10 #games on #Steam currently {TROPHY}\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        games_names.append(item[0])
        peak = item[1]['peak_players']
        message += ((f'{rank}-{item[0]} (Peak: {peak})\n'))
    return add_hashtags(message, games_names)


def create_message_trending_games(games):
    """Create a message for a tweet."""
    message = f'Top 5 trending #games on #Steam currently {TROPHY}\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        evolution = item[1]['evolution']
        games_names.append(item[0])
        message += ((f'{rank} {item[0]} (Evolution: {evolution} {CHART_INCREASING})\n'))
        message += '#' + ''.join(e for e in item[0] if e.isalnum()) + '\n'
    return add_hashtags(message, games_names)


def create_reply_message(games, tweet_type):
    """Create a reply message for a tweet."""
    if tweet_type == "trending":
        return add_hashtags(REPLY_MESSAGE_TRENDING, games)
    return add_hashtags(REPLY_MESSAGE_TOP, games)


def create_links_message(links, games):
    """Create a message to display links of games"""
    message = f'Links of the #games in the #leaderboard #today {TROPHY}\n\n'
    for i, link in enumerate(links):
        link = pyshorteners.Shortener().tinyurl.short(link)
        line = f'{games[i]} {link}\n'
        message += line
    return message


def add_hashtags(message, games):
    """add hashtags to the message"""
    message += '\n'
    for i in range(1, len(hashtags) // 4):
        hashtag = random.choice(hashtags)
        message += f'{hashtag} '
        if i % 4 == 0:
            message += '\n'
    # return the main message and the games names
    return message, games


def get_rank(rank):
    """getting the rank of the game"""
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
        while len(message) + len(messages[0]) < 270:
            message += messages[0] + '\n'
            messages.pop(0)
            if messages == []:
                break
        message += ARROW
        final_messages.append(message)
    return final_messages
