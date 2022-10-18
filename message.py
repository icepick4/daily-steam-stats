"""create a message for a tweet"""


def create_message_top_games(games):
    """Create a message for a tweet."""
    message = 'Top 5 #games on #Steam today \U0001F3C6\n\n'
    rank_one = ''
    for ctr, item in enumerate(games.items()):
        rank = get_rank(item[1]['rank'])
        if ctr == 0:
            rank_one = item[0]
        message += rank + '-' + item[0] + \
            ' (Peak: ' + \
            item[1]['peak_players'] + ')\n'
    message += '\n#SteamTop5 #Gaming #Trending #' + \
        ''.join(e for e in rank_one if e.isalnum())
    return message


def create_message_trending_games(games):
    """Create a message for a tweet."""
    message = 'Top 3 trending games on Steam today \U0001F3C6\n\n'
    rank_one = ''
    for ctr, item in enumerate(games.items()):
        rank = get_rank(item[1]['rank'])
        if ctr == 0:
            rank_one = item[0]
        message += rank + ' ' + item[0] + \
            ' (Evolution: ' + \
            item[1]['evolution'] + '\U0001f4c8' + ')\n'
    message += '\n#SteamTop3 #Gaming #Trending #' + \
        ''.join(e for e in rank_one if e.isalnum())
    return message


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
