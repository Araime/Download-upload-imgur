from auth import authenticate
from datetime import datetime
import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath


def upload_image(client, image_path, config):
	print("Uploading image... ")
	image = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")
	print()

	return image


if __name__ == "__main__":
	client = authenticate()
	album = 'Space-themed photos'

	#  вариант 1

	image_path = 'images/3861.jpg'
	config = {
		'album': album,
		'name': 'name',
		'description': 'Photo from internet {0}'.format(datetime.now())
	}
	image = upload_image(client, image_path, config)

	print("Image was posted!")
	print("You can find it here: {0}".format(image['link']))

	#  вариант 2

	# for image_name in listdir('.'):
	# 	if isfile:
	# 		name_for_split = os.path.splitext(image_name)
	# 		split_image_name = name_for_split[0]
	# 		image_path = image_name
	# 		config = {
	# 			'album': album,
	# 			'name': split_image_name,
	# 			'description': 'Photo from internet {0}'.format(datetime.now())
	# 		}
	# 		image = upload_image(client, image_path, config)
	#
	# 		print("Image was posted!")
	# 		print("You can find it here: {0}".format(image['link']))
