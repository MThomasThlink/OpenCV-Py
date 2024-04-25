import time
import cv2
import face_recognition
from Global import cascadePath

f1 = 'C:/Users/MThomas/PycharmProjects/OpenCV5/Fotos/Cam/ThomasCam0.jpg'
f2 = 'C:/Users/MThomas/PycharmProjects/OpenCV5/Fotos/Cam/xth088.jpg'
# f2 = 'C:\\WorkDir\\Luxand71\\lfw\\lfw\\Abba_Eban\\Abba_Eban_0001.jpg'

# img1 = cv2.imread(f1)
# img2 = cv2.imread(f2)
img1 = face_recognition.load_image_file(f1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = face_recognition.load_image_file(f2)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
# gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# wimg1 = gray1
# wimg2 = gray2

faceCascade = cv2.CascadeClassifier(cascadePath)
face1 = faceCascade.detectMultiScale(img1, scaleFactor=1.1, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,
                                         minSize=(0, 0), maxSize=(640, 640))
# face1 = face_recognition.face_locations(wimg1)

print('Face1: ', face1)
if len(face1) == 0:
    print('Faces não encontradas em Imagem1')
    exit(1)

for (x, y, w, h) in face1:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)

face2 = faceCascade.detectMultiScale(img2, scaleFactor=1.1, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,
                                     minSize=(0, 0), maxSize=(640, 640))
# face2 = face_recognition.face_locations(wimg2)
print('Face2: ', face2)
if len(face2) == 0:
    print('Faces não encontradas em Imagem2')
    exit(2)

for (x, y, w, h) in face2:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

start_time = time.time()
enc1 = face_recognition.face_encodings(img1, face1, num_jitters=0, model="small")
enc2 = face_recognition.face_encodings(img2, face2, num_jitters=0, model="small")

print("--- %s seconds ---" % (time.time() - start_time))
if len(enc1) >= 1:
    if len(enc2) >= 1:
        comp_result = face_recognition.compare_faces(enc1, enc2[0], tolerance=0.6)
        print('Comp: ', comp_result[0])

        dist_result = face_recognition.face_distance(enc1, enc2[0])
        print('Dist: ', dist_result[0])
    else:
        print('Imagem 2 não foi codificada')
else:
    print('Imagem 1 não foi codificada')

cv2.imshow('f1', img1)
cv2.imshow('f2', img2)
cv2.waitKey()
