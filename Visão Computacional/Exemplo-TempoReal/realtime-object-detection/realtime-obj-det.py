import cv2
from shapedetector import ShapeDetector

webcam = cv2.VideoCapture(0)
while True:
    _, frame = webcam.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()



