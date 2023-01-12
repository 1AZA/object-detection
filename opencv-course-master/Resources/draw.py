# drawing shapes and puttting text
import cv2 as cv 
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank )

# # paint thye image a certian colour 
# blank[:]= 0,255,0
# cv.imshow('Green', blank)

# draw a rectangle 
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('reactangle', blank )
# # draw a circle 
# cv.circle(blank ,(blank.shape[1]//2, blank.shape[0]//2), 40,(0,0,255),thickness=-1)
# cv.imshow('black',blank)

# # # 4. draw a line 
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('line',blank)

# write text 
cv.putText(blank, 'Mohammed Azam', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('TEXT', blank)


# img =cv.imread('Photos/cat.jpg')
# cv.imshow('cat', img)

cv.waitKey(0)

