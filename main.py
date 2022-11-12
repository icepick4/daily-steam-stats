"""main file"""
import sys
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
        print('Starting tweeting !')
        counter = 0
        while True:
            # if it's between 7am and 10pm tweet the peak of the day
            if 19 <= time.localtime().tm_hour <= 21:
                init_tweet_peak(debug)
                print('Tweeted the peak of the day')
            # tweet every 2 hours
            init_tweet_trending(debug)
            print('Tweeted trending games')
            time.sleep(60 * 5)
            init_tweet_top(debug)
            print('Tweeted top games')
            print('Waiting for next tweets... in 2 hours')
            time.sleep(60 * 60 * 2)
            counter += 1
    print('See the tweets on : https://twitter.com/DailySteamStats ')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--auto':
            main(False, False)
        elif sys.argv[1] == '--manual':
            main(True, False)
        elif sys.argv[1] == '--debug':
            main(True, True)
    else:
        print('Usage: python main.py --manual or --auto or --debug')
        sys.exit()
