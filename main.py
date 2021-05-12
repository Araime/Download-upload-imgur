import os
import requests
from pprint import pprint


def get_img(url, filename, directory):
    response = requests.get(url)
    response.raise_for_status()
    with open(directory + filename, 'wb') as file:
        file.write(response.content)
    return print('Ok.')


def get_launch_img(url_2, directory):
    response_2 = requests.get(url_2)
    response_2.raise_for_status()
    launch = response_2.json()
    launch_images = launch['links']['flickr_images']
    i = 1
    for image in launch_images:
        with open(directory + f'spacex{i}.jpg', 'wb') as file:
            file.write(response_2.content)
        i += 1
    return print('Ok.')


if __name__ == '__main__':
    directory = 'C:/Users/varfolomeyfever/PycharmProjects/Instagram photo/images/'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    url_2 = 'https://api.spacexdata.com/v3/launches/13'
    filename = 'hubble.jpeg'

    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        get_img(url, filename, directory)
    except requests.exceptions.HTTPError as error:
        exit(f'Введена неправильная ссылка:\n{error}')

    response_2 = requests.get(url_2)
    response_2.raise_for_status()
    launch = response_2.json()
    launch_images = launch['links']['flickr_images']

    # try:
    #     get_launch_img(url_2, directory)
    # except requests.exceptions.HTTPError as error:
    #     exit(f'Введена неправильная ссылка:\n{error}')
