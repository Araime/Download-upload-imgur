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
    for image_number, image in enumerate(launch_images):
        image_url = image
        response_3 = requests.get(image_url)
        response_3.raise_for_status()
        with open(directory + f'spacex{image_number + 1}.jpg', 'wb') as file:
            file.write(response_3.content)
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

    # response_2 = requests.get(url_2)
    # response_2.raise_for_status()
    # launch = response_2.json()
    # launch_images = launch['links']['flickr_images']
    #
    # pprint(type(launch))

    try:
        get_launch_img(url_2, directory)
    except requests.exceptions.HTTPError as error:
        exit(f'Введена неправильная ссылка:\n{error}')
