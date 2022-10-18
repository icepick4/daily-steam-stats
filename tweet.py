"""tweet a text and an image"""
import requests


def tweet(text, images, api):
    """Tweet a text and an image."""
    image = requests.get(images, allow_redirects=True)
    # file = open('tmp.png', 'wb').write(r.content)
    for i in range(len(images)):
        with open('./assets/tmp' + i + '.png', 'wb') as file:
            file.write(image.content)
    api.update_status_with_media(filename='tmp.png', status=text)
    print('Tweeted: ' + text)
