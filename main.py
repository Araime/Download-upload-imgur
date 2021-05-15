import os
import requests
from fetch_spacex import fetch_spacex_last_launch
from pprint import pprint
from urllib.parse import urlsplit, unquote_plus


def get_file_extension(image_link):
    segmented_url = urlsplit(image_link)
    file_path = segmented_url.path
    unquote_file_path = unquote_plus(string=file_path, encoding='utf-8', errors='Replace')
    split_file_and_path = os.path.split(unquote_file_path)
    split_file_and_extension = os.path.splitext(split_file_and_path[1])
    return split_file_and_extension[1]


def fetch_hubble(image_link, directory, image_id, extension):
    url = f'https:{image_link}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(directory + f'{image_id}{extension}', 'wb') as file:
        file.write(response.content)
    return print(f'Image with id {image_id} downloaded.')


if __name__ == '__main__':
    directory = os.getcwd() + '/images/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    hubble_url = 'http://hubblesite.org/api/v3/images/stsci_gallery'
    spacex_url = 'https://api.spacexdata.com/v3/launches/13'

    response = requests.get(hubble_url, verify=False)
    response.raise_for_status()
    image_collection_link = response.json()
    for image in image_collection_link:
        image_id = image['id']
        url = f'http://hubblesite.org/api/v3/image/{image_id}'
        response = requests.get(url)
        response.raise_for_status()
        hubble_response = response.json()
        image_link = hubble_response['image_files'][-1]['file_url']
        extension = get_file_extension(image_link)
        try:
            fetch_hubble(image_link, directory, image_id, extension)
        except requests.exceptions.HTTPError as error:
            exit(f'Введена неправильная ссылка:\n{error}')

    # try:
    #     fetch_spacex_last_launch(spacex_url, directory)
    # except requests.exceptions.HTTPError as error:
    #     exit(f'Введена неправильная ссылка:\n{error}')

    # image_id = 4522
    # ready_url = f'http://hubblesite.org/api/v3/image/4827'
    # extension = get_file_extension(ready_url)
