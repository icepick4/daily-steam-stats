# daily-steam-stats


<img src="https://img.shields.io/twitter/follow/DailySteamStats?label=Follow%20my%20bot%20%21%20%40DailySteamStats&style=for-the-badge" width="275">
<img src="https://img.shields.io/github/followers/icepick4?label=Follow%20me%20on%20GitHub%20%21%20@icepick4&style=for-the-badge" width="275">
<img src="https://img.shields.io/github/last-commit/icepick4/daily-steam-stats?style=for-the-badge" width="275">
<img src="https://forthebadge.com/images/badges/made-with-python.svg" width="225">
<img src="https://user-images.githubusercontent.com/82316285/197398864-cff7ae60-efdb-4858-ab13-54a861ed0dd1.svg" width="225">

## Description

This Twitter bot posts every day some tweets about trending games on steam.
You can take a look at it right [here](https://www.twitter.com/dailysteamstats)

## Dependencies

The bot depends on the following modules :

- requests
- tweepy
- bs4
- emoji
- pyshorteners

You can skip pyshorteners and emoji (it's a bonus for the bot)

Install them with the following command :

```
pip install -r requirements.txt
```

## Usages 

To use the scripts on your own, you must create a config.py file including your API keys. 
It claims that you already have a dev twitter account. If it's not the case, you will need one.

To post top games, use this in main.py
```python
# Pass True in arg to enter debug mode and avoid tweeting for real

init_tweet_top(False)
```

To post trending games, use this in main.py
```python
# Pass True in arg to enter debug mode and avoid tweeting for real

init_tweet_trending(False)
```
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




