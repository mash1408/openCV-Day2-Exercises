import cv2       # importing cv2
import numpy as np

img = cv2.imread('lightx.png')    # Reading an image

'''Create Translation Matrix'''
(h, w) = img.shape[:2] 
(q_h, q_w) =(int(h/4), int(w/4))
m = np.float32([[1, 0, q_w], [0, 1, 0]]) #shift right by quarter of its width


translated = cv2.warpAffine(img, m, (w, h))
cv2.imshow('Gradient B',translated)
cv2.waitKey(0)

m = np.float32([[1, 0, 0], [0, 1, q_h]]) #shift down by quarter of its height

translated = cv2.warpAffine(img, m, (w, h))
cv2.imshow('Gradient B',translated)
cv2.waitKey(0)

cv2.destroyAllWindows()