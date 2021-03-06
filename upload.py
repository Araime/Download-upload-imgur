from datetime import datetime
import os
from dotenv import load_dotenv
from imgurpython import ImgurClient


def authenticate(client_id, client_secret):
    client = ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url('pin')
    print(f'Go to the following URL: {authorization_url}')

    pin = input('Enter pin code: ')
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

    print('Authentication successful! Here are the details:')
    print(f'   Access token:  {credentials["access_token"]}')
    print(f'   Refresh token: {credentials["refresh_token"]}')

    return client


if __name__ == '__main__':
    load_dotenv()

    client_id = os.getenv('IMGUR_CLIENT_ID')
    client_secret = os.getenv('IMGUR_CLIENT_SECRET')
    client = authenticate(client_id, client_secret)

    album = None
    dirname = 'images'

    for image in os.listdir(dirname):
        if image.endswith(('.jpg', '.png')):
            filename, extension = os.path.splitext(image)
            image_path = os.path.join(dirname, image)
            config = {
                'album': album,
                'name': filename,
                'title': filename,
                'description': 'Photo from internet {0}'.format(datetime.now())
            }
            image = client.upload_from_path(image_path, config=config, anon=False)
