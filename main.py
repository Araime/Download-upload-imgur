import os
import requests


def get_pic(url, filename, directory):
    response = requests.get(url)
    response.raise_for_status()
    with open(directory + filename, 'wb') as file:
        file.write(response.content)
    return print('Ok.')


if __name__ == '__main__':
    directory = 'C:/Users/varfolomeyfever/PycharmProjects/Instagram photo/image/'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    filename = 'hubble.jpeg'

    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        get_pic(url, filename, directory)
    except requests.exceptions.HTTPError as error:
        exit(f'Введена неправильная ссылка:\n{error}')
