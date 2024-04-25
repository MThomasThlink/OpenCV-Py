import os
import cv2
import face_recognition
from Global import cascadePath
from PythonDB import dbins, dbclose, dbopen

# Cadastro de fotos (imagem para RGB)
def cadastro (folder):
    dbopen()
    arr = os.listdir(folder)
    # Detect faces in the image
    faceCascade = cv2.CascadeClassifier(cascadePath)
    # arr = ['th001.jpg']
    i = 0
    for fileName in arr:
        print('[{0:03d}] Arquivo: {1}. '.format(i, fileName))
        img = face_recognition.load_image_file(folder + '/' + fileName)
        # img = cv2.imread(BASE_PATH + '/' + fileName)
        # faces = faceCascade.detectMultiScale(
        #     rgb, scaleFactor=1.1, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE, minSize=(0, 0),
        #     maxSize=(640, 640))
        enc = face_recognition.face_encodings(img) #, faces, num_jitters=1, model="small")

        if len(enc) == 1:
            dbins(fileName, folder + '/' + fileName, enc[0])
        else:
            print('Erro')
        i = i + 1
        # if i >= 1:
        #     break

    print('Fim.')
    dbclose()
