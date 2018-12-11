import PIL
import os
from PIL import Image
from pathlib import Path

def resizingImage(path_to_image,basewidth,hsize,save_to_what):
    avCheck = Path(path_to_image)
    if avCheck.is_file():
        im = Image.open(path_to_image)
        im.thumbnail(basewidth)
        im.save(save_to_what,"JPEG")
        print("save image!")
    


bwidth = 256,256
hsizing = 256
counter = 51
for i in range(51,73):
    resizingImage("img//img//{}.jpg".format(str(counter).zfill(5)),bwidth,hsizing,"img//img//test//{}.jpg".format(str(counter-50)))
    #print(str(counter).zfill(5))
    counter+=1