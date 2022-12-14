# daily-steam-stats


<img src="https://img.shields.io/twitter/follow/DailySteamStats?label=Follow%20my%20bot%20%21%20%40DailySteamStats&style=for-the-badge" width="275">
<img src="https://img.shields.io/github/followers/icepick4?label=Follow%20me%20on%20GitHub%20%21%20@icepick4&style=for-the-badge" width="275">
<img src="https://img.shields.io/github/last-commit/icepick4/daily-steam-stats?style=for-the-badge" width="275">
<img src="https://forthebadge.com/images/badges/made-with-python.svg" width="225">
<img src="https://user-images.githubusercontent.com/82316285/197398864-cff7ae60-efdb-4858-ab13-54a861ed0dd1.svg" width="225">

## Description

This Twitter bot posts every day some tweets about trending games on steam.
You can take a look at it right [here](https://www.twitter.com/dailysteamstats)
Currently the bot is in auto mode, take a look just below in [Usages](#usages)
## Dependencies

The bot depends on the following modules :

- requests
- tweepy
- bs4
- emoji
- pyshorteners

You can skip pyshorteners and emoji (it's a bonus for the bot)

Install them with the following command :

```console
pip install -r requirements.txt
```

Datas are scraped from www.steamcharts.com

## Usages 

To use the scripts on your own, you must create a config.py file including your API keys. 
It claims that you already have a dev twitter account. If it's not the case, you will need one.

You have three ways to use the script :
```console
# post manually the tweets
python3 main.py --manual
# run the script without tweeting for real
python3 main.py --debug
# post every 2 hours automatically
python3 main.py --auto
```

- In auto mode, every two hours, the bot tweets trending games, then most played games, and once a day the peak games of the day.
- In manual mode you can choose which tweet you want.
- With debug mode you disable tweeting for real.

If you have any advice or any new feature idea just tell me !
Or simply fork this project and send me a pull request !

## Examples 

Currently tweets are threads containing :

- Main leaderboard
- Links to the games
- Hashtags
- Ending reply

### Screenshots 

Main leaderboard :

![image](https://user-images.githubusercontent.com/82316285/197399238-138e4040-dc8b-4cba-acda-403d59609e5b.png)
![image](https://user-images.githubusercontent.com/82316285/197399341-bda2ba8b-be00-4658-9f84-1ab586e6329d.png)
![image](https://user-images.githubusercontent.com/82316285/197399445-56d76586-cfaf-42dd-b5fa-5e8d62edc860.png)

Links to the games :

![image](https://user-images.githubusercontent.com/82316285/197399372-5daf6964-0f3c-40ac-b3b3-3c6fcd8cf76c.png)
![image](https://user-images.githubusercontent.com/82316285/197399468-d7481220-2583-47d7-bcb8-761dd31b6867.png)
![image](https://user-images.githubusercontent.com/82316285/197399478-6a6d9765-889b-4fb1-b30a-f97dbda79677.png)


Hashtags & Ending tweet :

![image](https://user-images.githubusercontent.com/82316285/197399417-35c94e07-13f5-40dc-92e9-b439ae88c1ee.png)




