# -*- coding: utf-8 -*-
"""
Created on Fri May 13 22:07:00 2022

@author: Almas Fathima
"""

from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2

import time


from imutils.video import FPS
from imutils.video import VideoStream


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-v", "--video", required=True,
	#help="path to input video file")

ap.add_argument("-c", "--confidence", type = float, default = 0.7)
args = vars(ap.parse_args())

file_name = "video location here"
window_name = "window"



labels = { 0: 'background',
            1: '', 2: '', 3: '', 4: '', 5: '', 6: '',
            7: '', 8: '', 9: '', 10: '', 11: '',
            13: '', 14: '', 15: '', 16: '', 17: '',
            18: '', 19: '', 20: '', 21: '', 22: '', 23: '',
            24: '', 25: '', 27: '', 28: '', 31: '',
            32: '', 33: '', 34: '', 35: '', 36: '',
            37: '', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
            41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
            46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
            51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
            56: 'broccoli', 57: 'carrot', 58: '', 59: 'pizza', 60: 'donut',
            61: 'cake', 62: '', 63: '', 64: '', 65: '',
            67: '', 70: '', 72: '', 73: 'laptop', 74: 'Plastic trash',
            75: 'Plastic trash', 76: 'Plastic trash', 77: 'Plastic trash', 78: '', 79: '',
            80: '', 81: '', 82: '', 84: 'book', 85: 'clock',
            86: 'vase', 87: 'scissors', 88: '', 89: 'Plastic trash', 90: 'Plastic trash' }

#mouse,remote,keyboard,cell phone,hair drier,toothbrush
colors = np.random.uniform(0, 255, size=(len(labels)+10, 3))
#prtxt = "ssd_inception_v2_coco_2017_11_17/graphFile.pbtxt"
#model = "ssd_inception_v2_coco_2017_11_17/frozen_inference_graph.pb"
prtxt = "ssd_mobilenet_v1_coco_11_06_2017/ssd_mobilenet_v1_coco.pbtxt"
model = "ssd_mobilenet_v1_coco_11_06_2017/frozen_inference_graph.pb"
#cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

#Loading Caffe Model
print('[Status] Loading Model...')

nn = cv2.dnn.readNetFromTensorflow(model, prtxt)
#Initialize Video Stream
print('[Status] Starting Video Stream...')
# open a pointer to the video stream and start the FPS timer
#vs = cv2.VideoCapture(args["video"])
video=input("Enter the video file name: ")
vs = cv2.VideoCapture(video)
time.sleep(2.0)
fps = FPS().start()

#Loop Video Stream

while True:
    _, frame = vs.read()
      
    frame = imutils.resize(frame, width=1500)
    (h, w) = frame.shape[:2]
    

    #Converting Frame to Blob
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 
    	0.007843, (300, 300), 127.5)

    #Passing Blob through network to detect and predict
    nn.setInput(blob)
    detections = nn.forward()


    #Loop over the detections
    for i in np.arange(0, detections.shape[2]):

	#Extracting the confidence of predictions
        confidence = detections[0, 0, i, 2]

        #Filtering out weak predictions
        if confidence > args["confidence"]:
            
            #Extracting the index of the labels from the detection
            #Computing the (x,y) - coordinates of the bounding box        
            idx = int(detections[0, 0, i, 1])

            #Extracting bounding box coordinates
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            #Drawing the prediction and bounding box
            label = "{}".format(labels[idx])
            cv2.rectangle(frame, (startX, startY), (endX, endY), colors[idx], 2)

            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    
    fps.update()

fps.stop()

print("[Info] Elapsed time: {:.2f}".format(fps.elapsed()))
print("[Info] Approximate FPS:  {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()
