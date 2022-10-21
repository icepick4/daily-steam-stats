"""constants"""
import emoji

URL = 'https://steamcharts.com/'

hashtags = ['#SteamTop', '#Gaming', '#Trending',
            '#SteamCharts', '#Stats', '#VideoGames',
            '#VR', '#Gamer', '#News', '#SteamTopGames',
            '#SteamTrendingGames', '#Steam', '#Leaderboard',
            '#Rank', '#BestGames', '#Charts', '#Players',
            '#Online', '#Datas', '#Statistics', '#SteamTrends',
            '#SteamTrendings', '#VideoGamesTrending', '#TT',
            '#BestSteamGames', '#SteamCharts', '#SteamChartsTop',
            '#SteamChartsTrending', '#Games', '#game', '#gaming',
            '#playstation', '#pc', '#twitch', '#esports', '#gamingcommunity',
            '#gamer']

LOGO_IMAGE = 'https://raw.githubusercontent.com/icepick4/daily-steam-stats/main/steam-logo.png'

CHART_INCREASING = emoji.emojize(':chart_increasing:')
TROPHY = emoji.emojize(':trophy:')
NUMBERS = [emoji.emojize(f':keycap_{i}:') for i in range(11)]
ARROW = emoji.emojize(':down_arrow:')

REPLY_MESSAGE_TRENDING = '#Games are ranked by their #evolution in the lasts 24 hours.\n\n'
REPLY_MESSAGE_TOP = '#Games are ranked by the number of #players on #Steam currently.\n\n'
