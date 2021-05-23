import os
from PIL import Image


if __name__ == '__main__':
    dirname = 'images'

    images_list = sorted(os.listdir(dirname))
    for img in images_list:
        if img.endswith(('.jpg', '.png')):
            split_filename = os.path.splitext(img)
            image_name = split_filename[0] + '.jpg'
            old_image_path = os.path.join(dirname, img)
            new_image_path = os.path.join(dirname, image_name)
            image = Image.open(old_image_path)
            image.thumbnail((1080, 1080))
            image.save(new_image_path, format='JPEG')
            if img.endswith('.png'):
                os.remove(old_image_path)
