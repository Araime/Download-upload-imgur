import os
from PIL import Image


if __name__ == '__main__':
    images_list = sorted(os.listdir('images'))
    for img in images_list:
        if img.endswith(('.jpg', '.png')):
            split_filename = os.path.splitext(img)
            image_name = split_filename[0]
            image = Image.open(f'images\\{img}')
            image.thumbnail((1080, 1080))
            image.save(f'images\\{image_name}.jpg', format='JPEG')
            if img.endswith('.png'):
                os.remove(f'images\\{img}')
