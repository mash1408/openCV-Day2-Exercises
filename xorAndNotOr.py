import cv2
import numpy as np
 
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), (255, 255, 255), -1)
cv2.imshow('f',rectangle)
cv2.waitKey(0)
 
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, (0, 0, 255), -1)
cv2.imshow('',circle)
cv2.waitKey(0)
# '''AND'''
# bitwiseAnd = cv2.bitwise_and(rectangle, circle)
# cv2.imshow('',bitwiseAnd)
# cv2.waitKey(0)

# '''OR'''
# bitwiseOr = cv2.bitwise_or(rectangle, circle)
# cv2.imshow('',bitwiseOr)
# cv2.waitKey(0)

'''NOT'''
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow('',bitwiseNot)
cv2.waitKey(0)

'''XOR'''
bitwiseXor = cv2.bitwise_xor(circle,rectangle)
cv2.imshow('',bitwiseXor)
cv2.waitKey(0)

cv2.destroyAllWindows()