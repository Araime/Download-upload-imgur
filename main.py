import os
import requests

directory = 'C:/Users/varfolomeyfever/PycharmProjects/Instagram photo/image/'

if not os.path.exists(directory):
    os.makedirs(directory)

filename = 'hubble.jpeg'
url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

response = requests.get(url)
response.raise_for_status()

with open(directory + filename, 'wb') as file:
    file.write(response.content)
