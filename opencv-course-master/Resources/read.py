# reading images 
import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('cat', img)

#reading vedios 
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('Vidio', frame )

    if cv.waitKey(20) & 0xFF==ord('d'):
        break 

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)


 
# When everything done, release
# the video capture object
#cv.release()
 
# Closes all the frames
#cv2.destroyAllWindows()