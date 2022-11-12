"""constants"""
import emoji

URL = 'https://steamcharts.com'

HASHTAGS = ['#SteamTop', '#Gaming', '#Trending',
            '#SteamCharts', '#Stats', '#VideoGames',
            '#VR', '#Gamer', '#News', '#SteamTopGames',
            '#SteamTrendingGames', '#Steam', '#Leaderboard',
            '#Rank', '#BestGames', '#Charts', '#Players',
            '#Online', '#Datas', '#Statistics', '#SteamTrends',
            '#SteamTrendings', '#VideoGamesTrending', '#TT',
            '#BestSteamGames', '#SteamCharts', '#SteamChartsTop',
            '#SteamChartsTrending', '#Games', '#game', '#gaming',
            '#playstation', '#pc', '#twitch', '#esports', '#gamingcommunity',
            '#gamer', '#gamers', '#gaminglife', '#gamingaddict', '#gamingsetup',
            '#gamingcommunity', '#gamingmemes', '#gamingpc', '#dataAnalytics',
            '#community', '#steamcommunity', '#steamcommunitygames', '#steamcommunitygifts',
            '#youtube', '#twitchstreamer', '#twitchstreamers', '#twitchstreaming',
            '#VirtualReality', '#VRGaming', '#VRGamer',
            '#VRGamingCommunity', '#VRGamingSetup',
            '#gameplay', '#developer', '#developers', '#developercommunity',
            '#developercommunitygames', '#gameDev', '#gameDevs',
            '#gameDevCommunity', '#gameDevCommunityGames',
            '#gameDevCommunityGifts']

LOGO_IMAGE = 'https://raw.githubusercontent.com/icepick4/daily-steam-stats/main/steam-logo.png'

CHART_INCREASING = emoji.emojize(':chart_increasing:')
CHART_DECREASING = emoji.emojize(':chart_decreasing:')
TROPHY = emoji.emojize(':trophy:')
NUMBERS = [emoji.emojize(f':keycap_{i}:') for i in range(11)]
DOWN_ARROW = emoji.emojize(':down_arrow:')
RIGHT_ARROW = emoji.emojize(':right_arrow:')
UP_ARROW = emoji.emojize(':up_arrow:')
PERSON = emoji.emojize(':person_frowning:')
SHOPPING_CART = emoji.emojize(':shopping_cart:')
GLOB = emoji.emojize(':globe_with_meridians:')
VIDEO_GAME = emoji.emojize(':video_game:')
SPARKLES = emoji.emojize(':sparkles:')
FIRE = emoji.emojize(':fire:')

REPLY_MESSAGE_TRENDING = '#Games are ranked by their #evolution in the lasts '\
    f'24 hours. {CHART_INCREASING}{TROPHY}\n\n'
REPLY_MESSAGE_TOP = '#Games are ranked by the number of #players on #Steam '\
    f'currently. {PERSON}{TROPHY}\n\n'
REPLY_MESSAGE_PEAK = '#Games are ranked by the #peak number of #players on #Steam today'\
    f'. {PERSON}{TROPHY}\n\n'
REPLY_MESSAGE_FOCUS = ''

END_MESSAGE = f'See the leaderbord {UP_ARROW}'
IDEAS_MESSAGE = f'If you have ideas to improve the tweets let me know!{SPARKLES}'
