"""tweet a text and an image"""
import os
import shutil

import requests


def tweet(message, images, api):
    """Tweet a message and an image."""
    media_ids = []
    filenames = []
    folder = './assets/'
    # empty this folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as error:
        print(f'Failed to delete {file_path}. Reason: {error}')
    for i, image in enumerate(images):
        req = requests.get(image, allow_redirects=True)
        filename = folder + 'tmp' + str(i + 1) + '.png'
        filenames.append(filename)
        with open(filename, 'wb') as file:
            file.write(req.content)

    # for filename in filenames:
    #     res = api.media_upload(filename)
    #     media_ids.append(res.media_id)

    # api.update_status(media_ids=media_ids, status=message)
    print('Tweeted: ' + message)
