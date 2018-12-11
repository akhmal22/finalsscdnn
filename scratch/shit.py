#!/usr/bin/env python

import numpy as np
import h5py

# Define a color palette
pal =  np.array([[0,     0, 168],
                 [0,     0, 252],
                 [0,   168, 252],
                 [84,  252, 252],
                 [168, 252, 168],
                 [0,   252, 168],
                 [252, 252,  84],
                 [252, 168,   0],
                 [252,   0,   0]],
                 dtype=np.uint8
               )

print(pal)

# Generate some data/image
x = np.linspace(0,pal.shape[0]-1)
data,Y = np.meshgrid(x,x)

# Create the HDF5 file
f = h5py.File('test.h5', 'w')

# Create the image and palette dataspaces
dset = f.create_dataset('img', data=data)
pset = f.create_dataset('palette', data=pal)

# Set the image attributes
dset.attrs['CLASS'] = 'IMAGE'
dset.attrs['IMAGE_VERSION'] = '1.2'
dset.attrs['IMAGE_SUBCLASS'] =  'IMAGE_INDEXED'
dset.attrs['IMAGE_MINMAXRANGE'] = np.array([0,255], dtype=np.uint8)
dset.attrs['PALETTE'] = pset.ref

# Set the palette attributes
pset.attrs['CLASS'] = 'PALETTE'
pset.attrs['PAL_VERSION'] = '1.2'
pset.attrs['PAL_COLORMODEL'] = 'RGB'
pset.attrs['PAL_TYPE'] = 'STANDARD8'

# Close the file
f.close()

f = h5py.File('test.h5', 'r')

dread = np.array(f['img'][:])
f.close()
print(dread.shape)