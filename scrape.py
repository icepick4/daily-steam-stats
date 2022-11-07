"""scrape steam top 100 games"""
import sys

import requests
from bs4 import BeautifulSoup

from constants import LOGO_IMAGE, URL


def get_games(trending):
    """Get the trending games from the Steam store."""
    try:
        page = requests.get(URL, headers={
                            'User-Agent': 'Mozilla/5.0'}, timeout=15).content
    except requests.exceptions.Timeout:
        print('Timeout error')
        sys.exit()
    except requests.exceptions.ConnectionError:
        print('Connection error')
        sys.exit()
    except requests.exceptions.HTTPError:
        print('HTTP error')
        sys.exit()
    soup = BeautifulSoup(page, 'html.parser')
    if trending:
        games = soup.select('table#trending-recent tbody tr')
        games = games[:5]
    else:
        games = soup.select('table#top-games tbody tr')
        games = games[:20]

    games_dict = {}
    for ctr, game in enumerate(games):
        name = game.select('a')[0].text
        name = name.replace('\t', '')
        name = name.replace('\n', '')
        rank = ctr + 1
        print(f'Getting data for {name}...')
        try:
            steam_link = get_steam_link('https://steamcharts.com' +
                                        game.select('a')[0]['href'])
        except IndexError:
            print('Could not get the steam link.')
            steam_link = 'https://example.com'
        image = get_image(steam_link)
        if trending:
            current_players = game.select('td')[3].text
            evolution = game.select('td')[1].text
            games_dict[name] = {
                'current_players': current_players,
                'evolution': evolution,
                'image': image,
                'rank': rank,
                'steam_link': steam_link
            }
        else:
            current_players = game.select('td')[2].text
            peak_players = game.select('td')[4].text
            games_dict[name] = {
                'current_players': current_players,
                'peak_players': int(peak_players),
                'image': image,
                'rank': rank,
                'steam_link': steam_link
            }
    return games_dict


def get_steam_link(image_page):
    """Get the steam link of a game."""
    try:
        image_page = requests.get(
            image_page, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15).content
    except requests.exceptions.Timeout:
        print('Timeout error')
        sys.exit()
    except requests.exceptions.ConnectionError:
        print('Connection error')
        sys.exit()
    except requests.exceptions.HTTPError:
        print('HTTP error')
        sys.exit()
    image_soup = BeautifulSoup(image_page, 'html.parser')
    return image_soup.select('#app-links a')[0]['href']


def get_image(steam_link):
    """Get the image of a game."""
    try:
        steam_soup = BeautifulSoup(requests.get(
            steam_link, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15).content, 'html.parser')
    except requests.exceptions.Timeout:
        print('Timeout error')
        sys.exit()
    except requests.exceptions.ConnectionError:
        print('Connection error')
        sys.exit()
    except requests.exceptions.HTTPError:
        print('HTTP error')
        sys.exit()
    image = steam_soup.select('img')
    steam_link_reference = 'https://cdn.akamai.steamstatic.com/steam/apps/'
    steam_link_reference_v2 = 'https://cdn.cloudflare.steamstatic.com/steam/apps/'

    for img in image:
        verify_type = 'header' in img['src'] and '.jpg' in img['src']
        verify_site = img['src'].startswith(
            steam_link_reference) or img['src'].startswith(steam_link_reference_v2)
        if verify_site and verify_type:
            return img['src']
    return LOGO_IMAGE
