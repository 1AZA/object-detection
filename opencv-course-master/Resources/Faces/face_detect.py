import cv2 as cv 

img = cv.imread('Photos/lady.jpg')
cv.imshow('lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('C:\Users\AZAM\OneDrive\Desktop\opencv-course-master\Section #3 - Faces')

faces_rect = cv.CascadeClassifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

print(f'Number of faces found ={len(faces_rect)}')

cv.waitKey(0)