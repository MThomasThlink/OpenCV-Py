#!/usr/bin/python3

import cv2
import face_recognition

# Create the haar cascade
from Global import cascadePath
from PythonDB import dbclose, dbopen, dbsearch

print('VidONE.py')
faceCascade = cv2.CascadeClassifier(cascadePath)

fotoCadastro = 'C:/Users/MThomas/PycharmProjects/OpenCV5/Fotos/Cam/dudu.jpg'
imgCadastro = face_recognition.load_image_file(fotoCadastro)    # exige conversão COLOR_BGR2RGB
imgCadastro = cv2.cvtColor(imgCadastro, cv2.COLOR_BGR2RGB)
# imgCadastro = cv2.imread(fotoCadastro)    # nao exige conversão

# imgCadastro = cv2.cvtColor(imgCadastro, cv2.COLOR_BGR2RGB)
# faceCadastro = faceCascade.detectMultiScale(imgCadastro, scaleFactor=1.1, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,
#                                     minSize=(0, 0), maxSize=(640, 640))
encCadastro = face_recognition.face_encodings(imgCadastro) #, faceCadastro, num_jitters=0, model="small")
cv2.imshow('Cadastro', imgCadastro)

ctd = 0
capture = cv2.VideoCapture(0)

while 1:
    ret, frame = capture.read()

    # Detect faces in the image
    # faceCapture = faceCascade.detectMultiScale(frame, scaleFctor=1.1, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,
    #    minSize=(0, 0), maxSize=(640, 640))

    # if len(faceCapture) > 0:
    encCapture = face_recognition.face_encodings(frame) #, faceCapture, num_jitters=1, model="small")
    if len(encCapture) == 1:
        dist_result = face_recognition.face_distance(encCapture, encCadastro[0])
        print('dist_result = ', dist_result)
    else:
        print('No capture enconding')
    # else:
    #     print('No capture faces')

    cv2.imshow('Camera', frame)
    k = cv2.waitKey(5) & 0xff
    if k == 113:
        break
    ctd = ctd + 1

print('Capture loop end.')
capture.release()
cv2.destroyAllWindows()
