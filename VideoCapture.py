import pyodbc
from cv2 import FONT_HERSHEY_COMPLEX_SMALL, imshow, waitKey, LINE_8, putText, destroyAllWindows, CascadeClassifier, \
    rectangle, LINE_AA, VideoCapture
import face_recognition
import time

from Global import cascadePath
from PythonDB import dbclose, dbopen, dbsearch


def camera_capture(cam_id):
    faceCascade = CascadeClassifier(cascadePath)
    dbopen()
    ctd = 0
    capture = VideoCapture(int(cam_id))

    while 1:
        ret, frame = capture.read()
        encodings = face_recognition.face_encodings(frame)  # , faces, num_jitters=1, model="small")
        if len(encodings) == 1:
            start_time = time.time()
            result = dbsearch(encodings[0], 1, 0.5)
            if result is not None:
                print("{0:.3f}ms. Found! Nome = {1}.".format(time.time() - start_time, result[1]))
                frame = rectangle(frame, (0, 0), (6400, 70), color=(0, 255, 0), thickness=-1)
                putText(frame, "Nome: {0}.".format(result[1]), org=(0, 30),
                        fontFace=FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 0, 0),
                        thickness=2, lineType=LINE_8)
                putText(frame, "Dist: {0:5.2}.".format(result[2]), org=(0, 60),
                        fontFace=FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 0, 0),
                        thickness=1, lineType=LINE_AA)
            else:
                print("{0:.3f}ms. NOT Found!".format(time.time() - start_time))
                # for (x, y, w, h) in faces:
                #    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        else:
            print('No enconding')
        # else:
        #         print('No faces')

        imshow("OpenCV @Python", frame)
        k = waitKey(5) & 0xff
        if k == 113:
            break
        ctd = ctd + 1

    print('Capture loop end.')
    capture.release()
    destroyAllWindows()
    dbclose()
