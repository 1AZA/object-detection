import cv2 as cv 

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('car', img)

def rescaleframe(frame, scale ):
    # method works for image , vedio, live vedio 
    width = int(frame.shape [1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height )

    return cv.resize(frame , dimensions, interpolation=cv.INTER_AREA)

def changeres(width , height):
    # method only for live vedio
    capture.set(3,width)
    capture.set(4,height)
    
    
#reading vedios 
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue , frame = capture.read()

    frame_resize = rescaleframe(frame, scale= 0.2)

    cv.imshow('Vidio', frame )
    cv.imshow('vedio resized', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('s'):
        break 

capture.release()
cv.destroyAllWindows()
#cv.waitKey(25)
 