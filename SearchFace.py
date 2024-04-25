import cv2
import face_recognition

from Global import cascadePath
from PythonDB import dbsearch, dbopen, dbclose, dbstring


def searchImage():
    # Detect faces in the image
    faceCascade = cv2.CascadeClassifier(cascadePath)

    # Define o nome do arquivo
    strFile1 = './Fotos/ThomasCamA.jpg'
    imgFR1 = face_recognition.load_image_file(strFile1)
    faces1 = faceCascade.detectMultiScale(
        imgFR1,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE,
        minSize=(0, 0),
        maxSize=(640, 640)
    )
    strFaces1 = "Found {0} faces!".format(len(faces1))
    thEnc1 = face_recognition.face_encodings(imgFR1, faces1, num_jitters=1)[0]
    result = dbsearch(thEnc1, 1)
    print(result)

dbopen()
print("Begin searchImage()")
searchImage()
print("End searchImage()")
dbclose()
