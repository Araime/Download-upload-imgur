from datetime import datetime
import os
from dotenv import load_dotenv
from imgurpython import ImgurClient
from os import listdir
from os.path import isfile
from os.path import join as joinpath

load_dotenv()

def authenticate():
	client_id = os.getenv('CLIENT_ID')
	client_secret = os.getenv('CLIENT_SECRET')
	client = ImgurClient(client_id, client_secret)

	authorization_url = client.get_auth_url('pin')
	print("Go to the following URL: {0}".format(authorization_url))

	pin = input("Enter pin code: ")
	credentials = client.authorize(pin, 'pin')
	client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

	print("Authentication successful! Here are the details:")
	print("   Access token:  {0}".format(credentials['access_token']))
	print("   Refresh token: {0}".format(credentials['refresh_token']))

	return client


def upload_image(client, image_path, config):
	print("Uploading image... ")
	image = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")
	print()

	return image


if __name__ == "__main__":
	# client = authenticate()
	album = 'Space-themed photos'
	image_path = 'images\\3861.jpg'
	print(image_path)

	# config = {
	# 	'album': album,
	# 	'name': 'name',
	# 	'description': 'Photo from internet {0}'.format(datetime.now())
	# }
	# image = upload_image(client, image_path, config)
	#
	# print("Image was posted!")
	# print("You can find it here: {0}".format(image['link']))

	# for image_name in listdir('.'):
	# 	if image_name.endswith(('.jpg', '.png')):
	# 		name_for_split = os.path.splitext(image_name)
	# 		split_image_name = name_for_split[0]
	# 		image_path = image_name
	# 		print(image_path)
			# config = {
			# 	'album': album,
			# 	'name': split_image_name,
			# 	'description': 'Photo from internet {0}'.format(datetime.now())
			# }
			# image = upload_image(client, image_path, config)
			#
			# print("Image was posted!")
			# print("You can find it here: {0}".format(image['link']))
