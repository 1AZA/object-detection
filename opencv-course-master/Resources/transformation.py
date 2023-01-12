import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow('group 1' , img )

# translation 

def translate(img , x , y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)

# -x --> left 
# -y --> up 
# x --> right 
# y --> down 

translate = translate(img , 100, 100 )
cv.imshow('translate', translate)

# rotation 
def rotated(img, angle, rotpoint=None):
    (height,width)= img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)

        rotmat = cv.getRotationMatrix2D(rotpoint, angle,1.0 )
        dimensions = (width, height )

        return cv.warpAffine(img, rotmat, dimensions)

rotate = rotated(img, -45) 
cv.imshow('rotated', rotate)       

rotated_rotated = rotated(rotate , -45)
cv.imshow('r_r', rotated_rotated)

# resize 
resize = cv.resize(img , (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resize)

# fliping 
flip = cv.flip(img , 1)
cv.imshow("flip" , flip)

# croping 
cropped = img[200:500,300:400]
cv.imshow('cropped', cropped)



cv.waitKey(0)
