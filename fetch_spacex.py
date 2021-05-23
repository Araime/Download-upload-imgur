import os
import argparse
import requests


def fetch_spacex_last_launch(spacex_url, directory):
    response = requests.get(spacex_url)
    response.raise_for_status()
    launch = response.json()
    photo_from_launch = launch['links']['flickr_images']
    for image_number, image_url in enumerate(photo_from_launch):
        response = requests.get(image_url)
        response.raise_for_status()
        with open(directory + f'spacex{image_number + 1}.jpg', 'wb') as file:
            file.write(response.content)
            print(f'Image spacex{image_number + 1}.jpg downloaded')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа принимает ссылку на фотографии запуска'
                                                 ' в качестве аргумента')
    parser.add_argument('link', help='Ссылка на фотографии запуска Spacex, например'
                                     ' https://api.spacexdata.com/v3/launches/13')
    args = parser.parse_args()
    spacex_url = args.link

    directory = os.getcwd() + '/images/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    fetch_spacex_last_launch(spacex_url, directory)
