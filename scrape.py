"""scrape steam top 100 games"""

import requests
from bs4 import BeautifulSoup

from constants import URL


def get_games(trending):
    """Get the trending games from the Steam store."""
    page = requests.get(URL, headers={
                        'User-Agent': 'Mozilla/5.0'}).content
    soup = BeautifulSoup(page, 'html.parser')
    if trending:
        games = soup.select('table#trending-recent tbody tr')
        games = games[:3]
    else:
        games = soup.select('table#top-games tbody tr')
        games = games[:5]

    games_dict = {}
    for ctr, game in enumerate(games):
        name = game.select('a')[0].text
        name = name.replace('\t', '')
        name = name.replace('\n', '')
        rank = ctr + 1
        image = get_image('https://steamcharts.com' +
                          game.select('a')[0]['href'])
        if trending:
            current_players = game.select('td')[3].text
            evolution = game.select('td')[1].text
            games_dict[name] = {
                'current_players': current_players,
                'evolution': evolution,
                'image': image,
                'rank': rank
            }
        else:
            current_players = game.select('td')[2].text
            peak_players = game.select('td')[4].text
            games_dict[name] = {
                'current_players': current_players,
                'peak_players': peak_players,
                'image': image,
                'rank': rank
            }
    return games_dict


def get_image(image_page):
    """Get the image of a game."""
    image_page = requests.get(
        image_page, headers={'User-Agent': 'Mozilla/5.0'}).content
    image_soup = BeautifulSoup(image_page, 'html.parser')
    return 'https://steamcharts.com' + image_soup.select('img.app-image')[0]['src']
