

import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'C:\Users\AZAM\OneDrive\Desktop\opencv-course-master\Resources\Faces\train'

# p = []
# for i in os.listdir(r'C:\Users\AZAM\OneDrive\Desktop\opencv-course-master\Resources\Faces\train'):
#     p.append(i)

# print(p)   
features = []
labels = []

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array , cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

            for(x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
print('Training done -------------------')

features = np.array(features, dtype='object')
labels= np .array(labels )

# print(f'Lenghth of the features= {len(features)}')
# print(f'Lenghth of the labels= {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and the labels list 
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
# np.save('features.npy', features)
# np.save('labels.npy',labels)






# haar_cascade = cv.CascadeClassifier('haar_face.xml')


   