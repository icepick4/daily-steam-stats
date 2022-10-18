"""scrape steam top 100 games"""
import json

import requests
from bs4 import BeautifulSoup

from constants import URL


def get_top_games():
    """Get the top 100 games from the Steam store."""
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}).content
    soup = BeautifulSoup(page, 'html.parser')
    top_games = soup.select('table#top-games tbody tr')
    top_games_dict = {}
    ctr = 0
    for game in top_games:
        name = game.select('a')[0].text
        name = ''.join(name.split())
        rank = ctr + 1
        current_players = game.select('td')[2].text
        peak_players = game.select('td')[4].text
        top_games_dict[name] = {
            'current_players': current_players,
            'peak_players': peak_players,
            'rank': rank
        }
        ctr += 1
    return top_games_dict


if __name__ == '__main__':
    data = get_top_games()
    print(json.dumps(data, indent=4))
