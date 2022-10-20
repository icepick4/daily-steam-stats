"""create a message for a tweet"""
import random

import pyshorteners

from constants import hashtags


def create_message_top_games(games):
    """Create a message for a tweet."""
    message = 'Top 6 #games on #Steam currently \U0001F3C6\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        games_names.append(item[0])
        message += ((f'{rank}-{item[0]} (Peak: ' +
                    item[1]['peak_players']) + ')\n')
    return add_hashtags(games_names, message)


def create_message_trending_games(games):
    """Create a message for a tweet."""
    message = 'Top 3 trending #games on #Steam currently \U0001F3C6\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        games_names.append(item[0])
        message += ((f'{rank} {item[0]} (Evolution: ' +
                    item[1]['evolution']) + '\U0001f4c8') + ')\n'
    return add_hashtags(games_names, message)


def create_reply_message(games):
    """Create a reply message for a tweet."""
    message = 'Games are ranked by the number of players on Steam currently or their evolution.'
    return add_hashtags(games, message)


def create_links_message(links, games):
    """Create a message to display links of games"""
    message = 'Links to the games:\n'
    for i, link in enumerate(links):
        link = pyshorteners.Shortener().tinyurl.short(link)
        line = f'{games[i]} {link}\n'
        message += line
    return add_hashtags(games, message)


def add_hashtags(games, message):
    """add hashtags to the message"""
    message += '\n'
    # add hashtags for each game name
    for game in games:
        game = ''.join(e for e in game if e.isalnum())
        message += ' #'
        message += game
    for _ in range(len(hashtags)):
        hashtag = random.choice(hashtags)
        message += f' {hashtag}'
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
        rank = str(rank)
    return rank


def cut_message(message):
    """cut the message into many messages with 280 characters"""
    messages = message.split('\n')
    final_messages = []
    return final_messages
