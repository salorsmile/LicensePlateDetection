# -*- coding: cp936 -*-
from RegionProp import colorSeg
import cv2
import numpy as np

n_pic = 502
i = 0

while i < n_pic:
    img = cv2.imread('H:\\����ͼ��\\Feature Training\\POS\\' \
                     + str(i) + '.jpg')
    sz0 = img.shape
    ratio = max(sz0) / 400.0
    img = cv2.resize(img, (int(sz0[1] / ratio), int(sz0[0] / ratio)))
    sz0 = img.shape
    img1 = colorSeg(img)
    img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    
    sz = list(sz0)
    sz[1] = sz[1] * 2
    sz = tuple(sz)
    img0 = np.zeros(sz, 'uint8')
    img0[:,0:sz0[1],:] = img
    img0[:,sz0[1]:,:] = img1
    cv2.imshow(str(i), img0)
    key = cv2.waitKey(0)
    if key == 32 or key == 27:
        break
    elif key == 2490368:
        i -= 2
        if i < -1:
            i = -1
    cv2.destroyAllWindows()
    i += 1

cv2.destroyAllWindows()
