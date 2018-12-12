import os
from pathlib import Path

itrd = 1
# adjust the range depends how long your data
for itr in range(1,23):
    if Path("scratch//test//square{}.jpg".format(str(itr))).is_file():
        os.rename("scratch//test//square{}.jpg".format(str(itr)),"scratch//test//square{}.jpg".format(str(itrd)))
        itrd+=1
