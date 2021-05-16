import os
from PIL import Image


if __name__ == '__main__':
    directory = os.getcwd() + '/images/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # images_list = sorted(os.listdir('Images/'))

    # for img in images_list:
    #     if img.endswith(('.jpg', '.png')):
    #         split_image_name = os.path.splitext(images_list[img])
    #         image_name = split_image_name[0]
    #         image = Image.open(f'images/{img}')
    #         image.thumbnail((1080, 1080))
    #         image.save(f'images/new {image_name}.jpg', format='JPEG')
