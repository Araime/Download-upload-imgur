import os
import argparse
import requests
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote_plus


def get_photo_link(url):
    response = requests.get(url)
    response.raise_for_status()
    photo_of_the_day = response.json()
    photo_link = photo_of_the_day['hdurl']
    return photo_link


def get_filename_and_extension(photo_link):
    splitted_url = urlsplit(photo_link)
    absolute_file_path = splitted_url.path
    unquote_file_path = unquote_plus(string=absolute_file_path, encoding='utf-8', errors='Replace')
    file_path, image_file = os.path.split(unquote_file_path)
    filename, file_extension = os.path.splitext(image_file)
    return filename, file_extension


def fetch_photo_of_the_day(directory, photo_link, filename, file_extension):
    response = requests.get(photo_link)
    response.raise_for_status()
    with open(f'{directory}{filename}{file_extension}', 'wb') as file:
        file.write(response.content)


def get_sheet_with_photo_links(url):
    sheet_with_links = []
    response = requests.get(url)
    response.raise_for_status()
    sheet_with_dataset = response.json()
    for dataset in sheet_with_dataset:
        photo_link = dataset['hdurl']
        sheet_with_links.append(photo_link)
    return sheet_with_links


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа принимает 4 необязательных аргумента '
                                                 'при запуске, читать readme')
    parser.add_argument('-d', '--date', help='Опциональный аргумент для загрузки по дате гггг-мм-дд',
                        nargs='?', default='')
    parser.add_argument('-s', '--several', help='Опциональный аргумент для загрузки нескольких фото',
                        nargs='?', default='')
    parser.add_argument('-sd', '--start_date', help='Опциональный аргумент, начальная дата гггг-мм-дд',
                        nargs='?', default='')
    parser.add_argument('-ed', '--end_date', help='Опциональный аргумент, конечная дата гггг-мм-дд',
                        nargs='?', default='')
    args = parser.parse_args()
    photo_date = args.date
    specifying_the_quantity = args.several
    photos_start_date = args.start_date
    photos_end_date = args.end_date

    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')

    directory = f'{os.getcwd()}/images/'
    os.makedirs(directory, exist_ok=True)

    base_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&'

    if specifying_the_quantity.find('several') != -1:
        url = f'{base_url}start_date={photos_start_date}&end_date={photos_end_date}'
        sheet_with_photos_links = get_sheet_with_photo_links(url)
        for photo_link in sheet_with_photos_links:
            filename, file_extension = get_filename_and_extension(photo_link)
            fetch_photo_of_the_day(directory, photo_link, filename, file_extension)
    else:
        url = f'{base_url}date={photo_date}'
        photo_link = get_photo_link(url)
        filename, file_extension = get_filename_and_extension(photo_link)
        fetch_photo_of_the_day(directory, photo_link, filename, file_extension)
