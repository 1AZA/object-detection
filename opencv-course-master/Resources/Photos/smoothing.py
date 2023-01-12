import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('cats', img)

# method of bluring 
# Averaging
average = cv.blur(img, (3,3))
cv.imshow("Average Blur" , average)

# gaussian blur 
blur2 = cv.GaussianBlur(img, (3,3),0)
cv.imshow("blur2" ,blur2)

# median blur 
median = cv.medianBlur(img ,3)
cv.imshow('median', median )

# bilateral 
bilateral = cv.bilateralFilter(img ,5,45,35 )
cv.imshow('bilateral img', bilateral)


cv.waitKey(0) 
