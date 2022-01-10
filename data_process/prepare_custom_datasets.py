"""
Resize image for training.
"""

import os
from PIL import Image

hr_dir = './hr_original_size/'
lr_dir = './lr_original_size/'

img_names = []
for img in os.listdir('./lr_original_size/'):
    if not img.endswith('.png'):
        continue
    img_names.append(img)

hr_size, lr_size = (192, 192), (64, 64)
for img_name in img_names:
    hr_path = os.path.join(hr_dir, img_name)
    lr_path = os.path.join(lr_dir, img_name)
    hr_img, lr_img = Image.open(hr_path), Image.open(lr_path)
    lr_img = Image.open(lr_path)
    w, h = lr_img.size
    hr_resize_img = hr_img.resize(hr_size)
    lr_resize_img = lr_img.resize(lr_size)
    hr_resize_img.save(os.path.join("./hr_192/", img_name))
    lr_resize_img.save(os.path.join("./lr_192/", img_name))
    print(f"img: {img_name} saved!")
