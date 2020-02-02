import numpy as np
import cv2 

#path = '/mnt/dataset_HDD/smitd/long/0074/half0001_4.npy' 
path = '/mnt/dataset_HDD/smitd/long/0096/half0001_5.npy'
file1 = np.load(path)
img= file1[0]
print(img.shape)
cv2.imwrite('test.png',img)

