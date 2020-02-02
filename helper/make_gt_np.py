# FIle to creat ground truth npy file out of a single long exposure image. Use only for DRV 

import numpy as np
import os 
import argparse
import glob
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--gt_folder',help='path to the gt folder',default='/mnt/dataset_HDD/smitd/long',type=str)
parser.add_argument('--short',default='/mnt/dataset_HDD/smitd/short1',type=str)
args = parser.parse_args()

DEBUG = False

def get_num(direc):
	return len([name for name in os.listdir(direc) if os.path.isfile(os.path.join(direc,name))])
	

for i,folder in enumerate(os.listdir(args.short)):
	gt_files = glob.glob(args.gt_folder+'/%s/half00*.png'%folder)
	gt_path = gt_files[0]
	num_frames = get_num(os.path.join(args.short,folder))
	im = cv2.imread(gt_path, cv2.IMREAD_UNCHANGED)
	tiled = np.tile(im,(num_frames,1,1,1))
	np.save(gt_path.split('.')[0] +'.npy',tiled)
	if DEBUG:
		print("image :",im.shape)
		print(tiled.shape)
		print('gt path',gt_path)
		print("Tiled path", gt_path.split('.')[0] +'.npy')
		if i == 4:
			break
		
