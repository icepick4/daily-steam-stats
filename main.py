"""main file"""
from tweet import init_tweet_top


def main():
    """main function"""
    # tweet the trending games
    # init_tweet_trending(False)
    # tweet the top games
    init_tweet_top(False)


if __name__ == '__main__':
    main()
