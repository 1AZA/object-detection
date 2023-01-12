import cv2 as cv  

import numpy as np 

blank =np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle', circle)

# basic bitwise AND --> intersecting regions 
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)

# bitwise XOR --> non- intersecting regions
bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_XOR',bitwise_XOR)

# bitwise NOT
bitwise_NOT = cv.bitwise_not(rectangle,circle)
cv.imshow('bitwise_not',bitwise_NOT)

cv.waitKey(0)


