import cv2 as cv
import numpy as np 
 
img = cv.imread('Photos/cats.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank )

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray , (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(img, 125,175)
cv.imshow('canny', canny)

# ret, tresh = cv.threshold(gray , 125, 255, cv.THRESH_BINARY)
# cv.imshow('tresh', tresh)

contours, hierarcies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1, (0,0,255),2)
cv.imshow('contours drawan' ,blank)

cv.waitKey(0) 