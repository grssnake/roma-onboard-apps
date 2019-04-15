from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
id = input('inter user id')
sampleNum = 0
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataSet/User." + str(id) + '.' + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
        image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Frame", image)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum > 20:
        break

    rawCapture.truncate(0)
