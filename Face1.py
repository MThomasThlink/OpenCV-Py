from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# Create the haar cascade
from Global import cascadePath

faceCascade = cv2.CascadeClassifier(cascadePath)

#imagePath = 'QrCodeTest.jpg'
imagePath = './Fotos/'
photoName = 'bradley.jpg'
image = cv2.imread(imagePath + photoName)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    flags=0,#.cv2.CV_HAAR_SCALE_IMAGE,
    minSize=(0, 0),
    maxSize=(640, 640)
)

strFaces = "Found {0} faces!".format(len(faces))
print(strFaces)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow(strFaces, image)
cv2.waitKey(0)
