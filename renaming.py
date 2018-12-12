import os
from pathlib import Path

itrd = 1
# adjust the range depends how long your data
for itr in range(0,394):
    if Path("gambar-ular//gambar-ular{}.jpg".format(str(itr+1))).is_file():
        os.rename("gambar-ular//gambar-ular{}.jpg".format(str(itr+1)),"gambar-ular//gambar-ular{}.jpg".format(str(itrd)))
        itrd+=1
        print("renamed")
    else:
        print("not available")
