"""main file"""
import time

from tweet import init_tweet_peak, init_tweet_top, init_tweet_trending


def main(manual, debug):
    """main function"""
    if manual:
        response = input('Press enter to tweet the trending games, s to skip')
        # tweet the trending games
        if response != 's':
            init_tweet_trending(debug)
        response = input('Press enter to tweet the top games, s to skip')
        # tweet the top games
        if response != 's':
            init_tweet_top(debug)
        response = input('Press enter to tweet the peak of the day, s to skip')
        # tweet the peak of the day
        if response != 's':
            init_tweet_peak(debug)
    else:
        while True:
            if time.localtime().tm_hour > 20:
                init_tweet_peak(debug)
                # tweet every 2 hours
            init_tweet_trending(debug)
            time.sleep(60 * 5)
            init_tweet_top(debug)
            print('Waiting for next tweet...')
            time.sleep(10800)


if __name__ == '__main__':
    OPTION = ''
    DEBUG = ''
    # you can choose to tweet mannually or automatically
    while OPTION not in ['y', 'n']:
        OPTION = input('Do you want to tweet manually (y/n)? ')
    while DEBUG not in ['y', 'n']:
        DEBUG = input('Do you want to debug (y/n)? ')
    DEBUG = DEBUG == 'y'
    if OPTION == 'y':
        main(True, DEBUG)
    else:
        main(False, DEBUG)
