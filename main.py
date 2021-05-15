import os
import requests
import argparse
from urllib.parse import urlsplit, unquote_plus


def get_image_link(ready_url):
    response = requests.get(ready_url)
    response.raise_for_status()
    hubble_response = response.json()
    link_for_downloading = hubble_response['image_files'][-1]['file_url']
    return link_for_downloading


def get_file_extension(image_link):
    segmented_url = urlsplit(image_link)
    file_path = segmented_url.path
    unquote_file_path = unquote_plus(string=file_path, encoding='utf-8', errors='Replace')
    split_file_and_path = os.path.split(unquote_file_path)
    split_file_and_extension = os.path.splitext(split_file_and_path[1])
    return split_file_and_extension[1]


def download_image(image_link, directory, image_id, extension):
    url = f'http:{image_link}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(directory + f'{image_id}{extension}', 'wb') as file:
        file.write(response.content)
    return print('Ok.')


if __name__ == '__main__':
    directory = os.getcwd() + '/images/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    parser = argparse.ArgumentParser(description='Программа для скачивания снимков, сделанных'
                                                 ' космическим телескопом Hubble')
    parser.add_argument('image_id', help='id изоображения для скачивания')
    args = parser.parse_args()

    image_id = args.image_id
    print(image_id)
    ready_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    image_link = get_image_link(ready_url)
    extension = get_file_extension(image_link)

    try:
        download_image(image_link, directory, image_id, extension)
    except requests.exceptions.HTTPError as error:
        exit(f'Введена неправильная ссылка:\n{error}')
