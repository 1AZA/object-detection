import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('group 1', img)

# converting to gray scale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


 
# blur image 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur )

# edge cascade 
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny' , canny)

# dilating the image 
dilated = cv.dilate(canny , (3,3) , iterations=3)
cv.imshow('dilated', dilated )

# eroding 
erode = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('erode', erode)

# resize 
resize = cv.resize(img , (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resize)

# croping 
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)