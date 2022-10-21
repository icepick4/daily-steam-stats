"""create a message for a tweet"""
import random

import pyshorteners

from constants import ARROW, CHART_INCREASING, NUMBERS, TROPHY, hashtags


def create_message_top_games(games):
    """Create a message for a tweet."""
    message = f'Top 10 #games on #Steam currently {TROPHY}\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        games_names.append(item[0])
        message += ((f'{rank}-{item[0]} (Peak: ' +
                    item[1]['peak_players']) + ')\n\n')
    return add_hashtags(games_names, message, True)


def create_message_trending_games(games):
    """Create a message for a tweet."""
    message = f'Top 3 trending #games on #Steam currently {TROPHY}\n\n'
    games_names = []
    for item in games.items():
        rank = get_rank(item[1]['rank'])
        games_names.append(item[0])
        message += ((f'{rank} {item[0]} (Evolution: ' +
                    item[1]['evolution']) + {CHART_INCREASING}) + ')\n\n'
    return add_hashtags(games_names, message, True)


def create_reply_message():
    """Create a reply message for a tweet."""
    message = '#Games are ranked by the number of #players'\
        'on #Steam currently or their #evolution in the lasts 24 hours.\n\n'
    return add_hashtags([], message, False)


def create_links_message(links, games):
    """Create a message to display links of games"""
    message = f'Links of the #games in the #leaderboard #today {TROPHY}\n\n'
    for i, link in enumerate(links):
        link = pyshorteners.Shortener().tinyurl.short(link)
        line = f'{games[i]} {link}\n'
        message += line
    return add_hashtags([], message, True)


def add_hashtags(games, message, only_games):
    """add hashtags to the message"""
    message += '\n'
    # add hashtags for each game name
    for game in games:
        game = ''.join(e for e in game if e.isalnum())
        message += ' #'
        message += game
    if only_games:
        return message, games
    for i in range(len(hashtags)):
        hashtag = random.choice(hashtags)
        message += f' {hashtag}'
        if i % 5 == 0:
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
