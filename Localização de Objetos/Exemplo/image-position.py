import numpy as np
import cv2

path = 'Localização de Objetos/Exemplo/bancada1.png'

def getElements(image):
    imgHSV = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2HSV)
    lower = np.array([32, 0, 0])
    upper = np.array([145, 255, 255])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(resizedImg, resizedImg, mask=mask)
    return imgResult

def showImages(images):
    for image in images:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def getPosition(image):
    img = image.copy()
    im_bw = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(im_bw, (5,5), 0)
    im_bw = cv2.Canny(blur, 10, 90)
    contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    centers = []
    for c in contours:
        M = cv2.moments(c)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(img, [c], -1, (0,255,0), 3)
            cv2.circle(img, (cx, cy), 5, (0,0,255), -1)
            cv2.putText(img, f"{cx, cy}", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            print(cx, cy)
    return img


img = cv2.imread(path)
resizedImg = cv2.resize(img, (640, 480))
maskedImage = getElements(resizedImg)
contoursImage = getPosition(maskedImage)
showImages([resizedImg, maskedImage, contoursImage])
