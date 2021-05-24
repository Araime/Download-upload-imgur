import os
from PIL import Image


if __name__ == '__main__':
    dirname = 'images'

    images_list = sorted(os.listdir(dirname))
    for img in images_list:
        split_filename = os.path.splitext(img)
        filename, extension = split_filename
        image = Image.open(os.path.join(dirname, img))
        image.thumbnail((1080, 1080))
        image.save(f'{os.path.join(dirname, filename)}.jpg', format='JPEG')
        if img.endswith('.png'):
            os.remove(os.path.join(dirname, img))
