import cv2 as cv 

img = cv.imread('Photos/cats.jpg')
cv.imshow('cats' , img )

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple Tresholding 
threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

threshold , thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('threshold_inv', thresh_inv)

# Adaptive tresholding 
adaptive = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,5)
cv.imshow('adaptive', adaptive)

cv.waitKey(0)