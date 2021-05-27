import os
from PIL import Image


if __name__ == '__main__':
    dirname = 'images'
    image_width = 1080
    image_height = 1080

    images_list = sorted(os.listdir(dirname))
    for img in images_list:
        if not img.endswith(('.jpg', '.png')):
            continue
        split_filename = os.path.splitext(img)
        filename, extension = split_filename
        image = Image.open(os.path.join(dirname, img))
        image.thumbnail((image_width, image_height))
        image.save(f'{os.path.join(dirname, filename)}.jpg', format='JPEG')
        if not img.endswith('.jpg'):
            os.remove(os.path.join(dirname, img))
