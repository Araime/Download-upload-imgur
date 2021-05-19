import os
from PIL import Image


if __name__ == '__main__':
    images_list = sorted(os.listdir('images/'))
    for img in images_list:
        if img.endswith(('.jpg', '.png')):
            split_image_name = os.path.splitext(img)
            image_name = split_image_name[0]
            image = Image.open(f'images/{img}')
            image.thumbnail((1080, 1080))
            image.save(f'images/{image_name}.jpg', format='JPEG')