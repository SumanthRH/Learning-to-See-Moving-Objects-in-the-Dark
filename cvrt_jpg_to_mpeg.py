import os
from os.path import join
import sys
import cv2
from skvideo.io import vwrite, vread
import numpy as np
from skimage.io import imread
import rawpy as rp
FOLDER = '/mnt/dataset_HDD/smitd/0001'
SAVE = './001.mp4'

filenames = sorted(os.listdir(FOLDER))
video = []
for filename in filenames:
	with rp.imread(join(FOLDER,filename)) as raw:
		img = raw.postprocess(demosaic_algorithm=False,half_size=True,output_color=rp.ColorSpace.raw,four_color_rgb=True)
		#img = raw.raw_image
		shape = (int(img.shape[1]/2.0),int(img.shape[0]/2.0))
		img = cv2.resize(img,dsize=shape)
		video.append(img)
#		print(img.shape,type(img))
	

'''for filename in filenames :
	image = imread(join(FOLDER,filename))
	video.append(image)'''
video = np.asarray(video)
#vwrite(SAVE,video)
np.save('./0_data/DRV/0001.npy',video)
'''video = np.load('0_data/Cam1/gain10.npy')

print(video.shape)'''

