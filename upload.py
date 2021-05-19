from datetime import datetime
import os
from dotenv import load_dotenv
from imgurpython import ImgurClient

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
	image_status = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")
	print()

	return image_status


if __name__ == "__main__":
	client = authenticate()
	album = None
	dirname = 'images'

	for image in os.listdir(dirname):
		if image.endswith(('.jpg', '.png')):
			name_for_split = os.path.splitext(image)
			split_image_name = name_for_split[0]
			image_path = os.path.join(dirname, image)
			print(image_path)
			config = {
				'album': album,
				'name': split_image_name,
				'title': split_image_name,
				'description': 'Photo from internet {0}'.format(datetime.now())
			}
			image_response = upload_image(client, image_path, config)

			print("Image was posted!")
			print("You can find it here: {0}".format(image_response['link']))
