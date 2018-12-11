import h5py
import numpy as np
import PIL
from pathlib import Path
from PIL import Image

def jpg_image_to_array(path_to_image):
    '''
        thanks to awnihannun
    '''
    avCheck = Path(path_to_image)
    if avCheck.is_file():
        with Image.open(path_to_image) as image:
            im_arr = np.fromstring(image.tobytes(),dtype=np.uint8)
            im_arr = im_arr.reshape((image.size[1],image.size[0],3))
            
        return im_arr
    


a = np.asarray([jpg_image_to_array("train//{}.jpg".format(str(1)))])
ac = np.asarray([jpg_image_to_array("train//{}.jpg".format(str(2)))])
bool_m = a == ac[1,:]
subset = raw_data[bool_m]
#print(jpg_image_to_array("train//{}.jpg".format(str(1))))
#counter = 0
#for itr in range(0,51):
#    a[counter] = jpg_image_to_array("train//{}.jpg".format(str(itr+1).zfill(5)))
#    counter+=1
print(subset)
for itr in range(0,51):
    jpg_image_to_array("train//{}.jpg".format(str(itr+1)))
    #np.insert(salju_arr,itr,itr)
    #imga = jpg_image_to_array("img//img//{}.jpg".format(str(counter+1).zfill(5)))

#print(salju_arr)

#f = h5py.File('train_salju.h5','a')
#f.create_dataset('set_x_tr', data=salju_arr)


#train_dataset = h5py.File('train_salju.h5', "r")
#train_set_x_orig = np.array(train_dataset["set_x_tr"][:]) # your train set features

#print(train_set_x_orig)
