"""main file"""
import time

from tweet import init_tweet_top, init_tweet_trending


def main(manual):
    """main function"""
    if manual:
        input('Press enter to tweet the trending games')
        # tweet the trending games
        init_tweet_trending(False)
        # tweet the top games
        input('Press enter to tweet the top games')
        init_tweet_top(False)
    else:
        while True:
            # tweet every 2 hours
            init_tweet_trending(False)
            time.sleep(60 * 5)
            init_tweet_top(False)
            print('Waiting for next tweet...')
            time.sleep(10800)


if __name__ == '__main__':
    OPTION = ''
    # you can choose to tweet mannually or automatically
    while OPTION not in ['y', 'n']:
        OPTION = input('Do you want to tweet manually (y/n)? ')
    if OPTION == 'y':
        main(True)
    else:
        main(False)
