
from skimage import io,color
import numpy as np
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(
                    prog='BrillCrop',
                    description='Crops at the yellow square of the image saved from the LightMachinery device. Please input the filename of the brightfield image (intended to be a RGB image with a yellow square)',
                    epilog='Developed at CeMi - glagow.thecemi.org')

parser.add_argument('filename')
args = parser.parse_args()
      
fname = Path(args.filename)

image = io.imread(fname)
hsv = color.convert_colorspace(image,'RGB','YUV')

tomask = hsv[:,:,2]
x,y = np.where( tomask==np.max(tomask))
start = (np.min(x)+1,np.min(y)+1)
stop = (np.max(x)-1,np.max(y)-1)

brightfield = color.rgb2gray(image)
myimage = image[start[0]:stop[0],start[1]:stop[1]]

newname = fname.stem + '_cropped.tif'
newfname = fname.parent / newname

io.imsave(newfname,myimage)