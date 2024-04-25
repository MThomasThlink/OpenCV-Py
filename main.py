from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
import face_recognition

from Global import cascadePath
from PythonDB import dbopen, dbclose, dbins

print('OpenCV5.')

dbopen()

# Detect faces in the image
faceCascade = cv2.CascadeClassifier(cascadePath)

# Define o nome do arquivo
strFile1 = './Fotos/ThomasCamA.jpg'
strFile2 = './Fotos/ThomasCamB.jpg'
strFile3 = './Fotos/Dudu.jpg'
print('Arquivos: ', strFile1, strFile2, strFile3)

# Carrega foto usando face_recognition.load_image_file
imgFR1 = face_recognition.load_image_file(strFile1)
imgFR2 = face_recognition.load_image_file(strFile2)
imgFR3 = face_recognition.load_image_file(strFile3)

faces1 = faceCascade.detectMultiScale(
    imgFR1,
    scaleFactor=1.1,
    minNeighbors=5,
    flags=cv2.CASCADE_SCALE_IMAGE,
    minSize=(0, 0),
    maxSize=(640, 640)
)
faces2 = faceCascade.detectMultiScale(
    imgFR2,
    scaleFactor=1.1,
    minNeighbors=5,
    flags=0,  # .cv2.CV_HAAR_SCALE_IMAGE,
    minSize=(0, 0),
    maxSize=(640, 640)
)
faces3 = faceCascade.detectMultiScale(
    imgFR3,
    scaleFactor=1.1,
    minNeighbors=5,
    flags=0,  # .cv2.CV_HAAR_SCALE_IMAGE,
    minSize=(0, 0),
    maxSize=(640, 640)
)

strFaces1 = "Found {0} faces!".format(len(faces1))
# print(strFaces1)
strFaces2 = "Found {0} faces!".format(len(faces2))
# print(strFaces1)
strFaces3 = "Found {0} faces!".format(len(faces3))
# print(strFaces3)

# Cria o encode da foto (para gravar e comparar no futuro
thEnc1 = face_recognition.face_encodings(imgFR1, faces1, num_jitters=1)[0]
dbins('Marcelo Thomas Cam1', strFile1, thEnc1)
# print(thEnc1)
thEnc2 = face_recognition.face_encodings(imgFR2, faces2, num_jitters=1)[0]
dbins('Marcelo Thomas Cam2', strFile2, thEnc2)
# print(thEnc2)
# thEnc3 = face_recognition.face_encodings(imgFR3, faces3, num_jitters=1)[0]
# print(thEnc3)

# Draw a rectangle around the faces
# for (x, y, w, h) in faces1:
#     cv2.rectangle(imgFR1, (x, y), (x + w, y + h), (0, 255, 0), 2)
# for (x, y, w, h) in faces2:
#     cv2.rectangle(imgFR2, (x, y), (x + w, y + h), (0, 255, 0), 2)
# for (x, y, w, h) in faces3:
#     cv2.rectangle(imgFR3, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.namedWindow('ThCam1')
# cv2.namedWindow('ThCam2')
# cv2.namedWindow('ThCam3')
#
# cv2.imshow('ThCam1', imgFR1)
# cv2.imshow('ThCam2', imgFR2)
# cv2.imshow('ThCam3', imgFR3)
#

# Comparar 1 com 2
res12 = face_recognition.compare_faces([thEnc1], thEnc2)
# res13 = face_recognition.compare_faces([thEnc1], thEnc3)
# res23 = face_recognition.compare_faces([thEnc2], thEnc3)

dist12 = face_recognition.face_distance([thEnc1], thEnc2)
print('Dist 1-2: ', dist12)
# dist13 = face_recognition.face_distance([thEnc1], thEnc3)
# print('Dist 1-3: ', dist13)
# dist23 = face_recognition.face_distance([thEnc2], thEnc3)
# print('Dist 2-3: ', dist23)

dbclose()
cv2.waitKey(0)



# Carrega foto e converte para tons de cinza
# img = cv2.imread(strFile, cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
