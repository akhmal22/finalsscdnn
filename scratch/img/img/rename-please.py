import os

try:
    counter = 1
    for x in (0,3):
        os.rename("{}.jpg".format(str(counter).zfill(5)),"{}.jpg".format(str(x)))
        counter+=1

except: 
    counter+=1
