import os
from PIL import Image


def get_processing_image(dirname, image_width, image_height):
    for img in images_list:
        if not img.endswith(('.jpg', '.png')):
            continue
        split_filename = os.path.splitext(img)
        filename, extension = split_filename
        image = Image.open(os.path.join(dirname, img))
        image.thumbnail((image_width, image_height))
        image.save(f'{os.path.join(dirname, filename)}.jpg', format='JPEG')


def deleting_unnecessary_images(dirname, images_list):
    for img in images_list:
        if not img.endswith('.jpg'):
            os.remove(os.path.join(dirname, img))


if __name__ == '__main__':
    dirname = 'images'
    images_list = sorted(os.listdir(dirname))
    image_width = 1080
    image_height = 1080

    get_processing_image(dirname, image_width, image_height)
    deleting_unnecessary_images(dirname, images_list)
