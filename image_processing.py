import os
from PIL import Image


def processing_images(dirname, images, image_width, image_height):
    for img in images:
        if not img.endswith(('.jpg', '.png')):
            continue
        filename, extension = os.path.splitext(img)
        image = Image.open(os.path.join(dirname, img))
        image.thumbnail((image_width, image_height))
        image.save(f'{os.path.join(dirname, filename)}.jpg', format='JPEG')


def delete_unnecessary_images(dirname, images):
    for img in images:
        if not img.endswith('.jpg'):
            os.remove(os.path.join(dirname, img))


if __name__ == '__main__':
    dirname = 'images'
    images = sorted(os.listdir(dirname))
    image_width = 1080
    image_height = 1080

    processing_images(dirname, images, image_width, image_height)
    delete_unnecessary_images(dirname, images)
