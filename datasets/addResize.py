import time
import numpy as np
import h5py
import scipy
from PIL import Image
from pathlib import Path
import cv2

def make_square(path_to_img):
    '''
        thanks to stephen rauch, jdhao
    '''
    desired_size = 64
    im_pth = path_to_img
    im = Image.open(im_pth)
    old_size = im.size  # old_size[0] is in (width, height) format
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # use thumbnail() or resize() method to resize the input image
    # thumbnail is a in-place operation
    # im.thumbnail(new_size, Image.ANTIALIAS)
    im = im.resize(new_size, Image.ANTIALIAS)
    # create a new image and paste the resized on it
    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                        (desired_size-new_size[1])//2))
    return new_im

for itr in range(301,374):
    if Path("gambar-ular//gambar-ular{}.jpg".format(str(itr))).is_file():
        imsq = make_square("gambar-ular//gambar-ular{}.jpg".format(str(itr)))
        imsq.save("datasets//test//gambar-ularsq{}.jpg".format(str(itr)))
        print("oke")
    else:
        print("nah")