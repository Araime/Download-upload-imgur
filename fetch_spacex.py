import os
import argparse
import requests


def fetch_spacex_launch(launch_number, directory):
    url = f'https://api.spacexdata.com/v3/launches/{launch_number}'
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()
    photo_from_launch = launch['links']['flickr_images']
    for image_number, image_url in enumerate(photo_from_launch):
        response = requests.get(image_url)
        response.raise_for_status()
        with open(f'{directory}spacex{image_number + 1}.jpg', 'wb') as file:
            file.write(response.content)
            print(f'Image spacex{image_number + 1}.jpg downloaded')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа принимает ссылку на номер запуска'
                                                 ' в качестве аргумента и скачивает сотографии')
    parser.add_argument('launch_number', help='Номер запуска Spacex, например 13')
    args = parser.parse_args()
    launch_number = args.launch_number

    directory = f'{os.getcwd()}/images/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    fetch_spacex_launch(launch_number, directory)
