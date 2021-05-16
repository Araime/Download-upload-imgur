import requests


def fetch_spacex_last_launch(spacex_url, directory):
    response_2 = requests.get(spacex_url)
    response_2.raise_for_status()
    launch = response_2.json()
    launch_images = launch['links']['flickr_images']
    for image_number, image in enumerate(launch_images):
        image_url = image
        response_3 = requests.get(image_url)
        response_3.raise_for_status()
        with open(directory + f'spacex{image_number + 1}.jpg', 'wb') as file:
            file.write(response_3.content)
            print(f'Image spacex{image_number + 1}.jpg downloaded')
    return print('Process completed')
