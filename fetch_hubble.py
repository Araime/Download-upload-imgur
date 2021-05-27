import os
import argparse
import requests
from urllib.parse import urlsplit, unquote_plus


def get_collection(hubble_url):
    response = requests.get(hubble_url, verify=False)
    response.raise_for_status()
    collection = response.json()
    return collection


def get_file_extension(image_link):
    splitted_url = urlsplit(image_link)
    absolute_file_path = splitted_url.path
    unquote_file_path = unquote_plus(string=absolute_file_path, encoding='utf-8', errors='Replace')
    file_path, image_file = os.path.split(unquote_file_path)
    filename, file_extension = os.path.splitext(image_file)
    return file_extension


def fetch_hubble_image(image_link, directory, image_id, extension):
    url = f'https:{image_link}'
    response_image = requests.get(url, verify=False)
    response_image.raise_for_status()
    with open(f'{directory}{image_id}{extension}', 'wb') as file:
        file.write(response_image.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа принимает название коллекции фотографий'
                                                 ' в качестве аргумента')
    parser.add_argument('collection_name', help='Название коллекции фотографий Hubble', nargs='?',
                        default='stsci_gallery')
    args = parser.parse_args()
    hubble_url = f'https://hubblesite.org/api/v3/images/{args.collection_name}'

    directory = f'{os.getcwd()}/images/'
    os.makedirs(directory, exist_ok=True)

    collection = get_collection(hubble_url)

    for image in collection:
        image_id = image['id']
        ready_url = f'https://hubblesite.org/api/v3/image/{image_id}'
        response = requests.get(ready_url)
        response.raise_for_status()
        hubble_response = response.json()
        image_link = hubble_response['image_files'][-1]['file_url']
        extension = get_file_extension(image_link)
        fetch_hubble_images(image_link, directory, image_id, extension)
