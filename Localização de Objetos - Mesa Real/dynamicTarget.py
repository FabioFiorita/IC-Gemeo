from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots
from tkinter import *
import numpy as np
import cv2

def getElements(image):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([32, 0, 0])
    upper = np.array([145, 255, 255])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(image, image, mask=mask)
    return imgResult

def showImages(images):
    for image in images:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def getPosition():
    path = '/home/fabiofiorita/Documentos/IC-Gemeo/Localização de Objetos/DynamicTarget/bancada1.png'
    image = cv2.imread(path)
    #image = cv2.resize(image, (1200, 2000))
    maskedImage = getElements(image)
    
    img = maskedImage.copy()
    im_bw = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #blur = cv2.GaussianBlur(im_bw, (5,5), 0)
    #im_bw = cv2.Canny(blur, 10, 90)
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
            centers.append((cx, cy))
    showImages([image, maskedImage, img])
    return centers

def interface():
    centers = getPosition()

    master = Tk()
    master.geometry("400x400")
    master.title("Localização de Objetos")
    master.eval('tk::PlaceWindow . center')


    t = Text(master, height=10, width=10)
    for x in centers:
        t.insert(END, x)
        t.insert(END, "\n")
    t.pack()

    indexes = []
    j = 0
    for _ in centers:
        indexes.append(j)
        j += 1
    
    variable = StringVar(master)
    variable.set(indexes[0])

    w = OptionMenu(master, variable, *indexes)
    w.pack()


    def ok():
        result = variable.get()
        print ("value is: " + result)
        print(centers[int(result)])
        global cx, cy
        cx, cy = centers[int(result)]
        master.destroy()

    button = Button(master, text="OK", command=ok)
    button.pack()

    mainloop()
    return cx, cy

RL = Robolink()

robot = RL.Item('Staubli TS60 FL 200')
world = RL.Item('World')
retract = RL.Item('Retract')
areaTrabalho = RL.Item('AreaTrabalho')

target = RL.AddTarget('Cube', areaTrabalho)
cx, cy = interface()
print(cx, cy)
RL.ShowMessage('Centers: ' + str(cx) + ' ' + str(cy))
target.setPose(Offset(eye(), cx, cy, 0, 0, 180, 0))

robot.MoveJ(retract)
robot.MoveJ(target)
robot.MoveJ(retract)