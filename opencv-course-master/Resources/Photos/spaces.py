import cv2 as cv 

import matplotlib.pyplot as plt 

img = cv.imread('Photos/park.jpg')
cv.imshow('park', img)

# plt.imshow(img)
# plt.show()

# # BGR to Grayscale 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray scale' , gray)

# bgr = cv.cvtColor(gray, cv.COLOR_BGR2GRAY)
# cv.imshow('bgr', bgr) 

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

# BGR to RGB 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('BGR2RGB', rgb)

# HSV to BGR 
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR, )
cv.imshow('bgt2hsv', bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)