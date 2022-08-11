import cv2
import numpy as np

path = 'Localização de Objetos/Exemplo/bancada1.png'

cv2.namedWindow('Bancada')
cv2.resizeWindow('Bancada', (640, 240))
cv2.createTrackbar('Hue min', 'Bancada', 32, 179, lambda x: None)
cv2.createTrackbar('Hue max', 'Bancada', 145, 179, lambda x: None)
cv2.createTrackbar('Sat min', 'Bancada', 0, 255, lambda x: None)
cv2.createTrackbar('Sat max', 'Bancada', 255, 255, lambda x: None)
cv2.createTrackbar('Val min', 'Bancada', 0, 255, lambda x: None)
cv2.createTrackbar('Val max', 'Bancada', 255, 255, lambda x: None)

while True:
    img = cv2.imread(path)
    resizedImg = cv2.resize(img, (640, 480))
    imgHSV = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue min', 'Bancada')
    h_max = cv2.getTrackbarPos('Hue max', 'Bancada')
    s_min = cv2.getTrackbarPos('Sat min', 'Bancada')
    s_max = cv2.getTrackbarPos('Sat max', 'Bancada')
    v_min = cv2.getTrackbarPos('Val min', 'Bancada')
    v_max = cv2.getTrackbarPos('Val max', 'Bancada')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(resizedImg, resizedImg, mask=mask)
    

    cv2.imshow('Original',img)
    cv2.imshow('HSV',imgHSV)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',imgResult)
    cv2.waitKey(1)