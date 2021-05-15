import requests

def fetch_hubble(image_link, directory, image_id, extension):
    url = f'https:{image_link}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(directory + f'{image_id}{extension}', 'wb') as file:
        file.write(response.content)
    return print(f'Image with id {image_id} downloaded.')
