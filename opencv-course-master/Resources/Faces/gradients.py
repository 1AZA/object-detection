import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('cats' , img )

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# sobel
sobelx = cv.Sobel(gray , cv.CV_64F , 0, 1)
sobley = cv.Sobel(gray , cv.CV_64F, 1 ,0 )
combined = cv.bitwise_or(sobelx, sobley)

cv.imshow('sobel X' , sobelx)
cv.imshow('soble Y' , sobley)
cv.imshow('combined', combined)

canny = cv.Canny(gray, 100, 175 )
cv.imshow('canny', canny)

cv.waitKey(0)