"""tweet a text and an image"""
import os
import shutil
from pathlib import Path

import requests


def tweet(message, images, api, debug=False):
    """Tweet a message and an image."""
    filenames = []
    folder = './assets/'
    dir_path = Path(folder)
    try:
        shutil.rmtree(dir_path)
        os.mkdir(folder)
    except OSError as error:
        print(f'Failed to delete {folder}. Reason: {error}')

    for i, image in enumerate(images):
        req = requests.get(image, allow_redirects=True)
        filename = f'{folder}tmp{str(i + 1)}.png'
        filenames.append(filename)
        with open(filename, 'wb') as file:
            file.write(req.content)

    if not debug:
        media_ids = []
        for filename in filenames:
            res = api.media_upload(filename)
            media_ids.append(res.media_id)
        api.update_status(media_ids=media_ids, status=message)
    print(f'Tweeted: {message}')
