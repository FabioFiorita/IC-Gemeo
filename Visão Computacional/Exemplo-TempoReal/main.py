from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots
import cv2
import imutils

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		# if the shape is a triangle, it will have 3 vertices else it's a rectangle
		if len(approx) == 3:
			shape = "triangle"
		else:
			shape = "square"

		# return the name of the shape
		return shape

def getShape():
    webcam = cv2.VideoCapture(0)
    while True:
        _, frame = webcam.read()
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()

    cv2.imshow('Webcam', frame)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    return frame

def detectShape():
    # load the image and resize it to a smaller factor so that
    # the shapes can be approximated better
    image = getShape()
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()

    # loop over the contours
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)

        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2)

        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)
    return shape

RL = Robolink()

robot = RL.Item('KUKA KR 6 R900 sixx')

app_InspectA = RL.Item('App_InspectA')
retract_InspectA = RL.Item('Retract_InspectA')

def moveRobot(shape):
    robot.MoveJ(app_InspectA)
    if shape == "triangle":
        moveTriangle()
    else:
        moveSquare()
    robot.MoveJ(retract_InspectA)
    
def moveTriangle():
    for i in range(1, 4):
        targetName = f"Triangle {i}"
        robot.MoveJ(RL.Item(targetName))
    robot.MoveJ(RL.Item("Triangle 1"))

def moveSquare():
    for i in range(1, 5):
        targetName = f"Square {i}"
        robot.MoveJ(RL.Item(targetName))
    robot.MoveJ(RL.Item("Square 1"))

for i in range(2):
    shape = detectShape()
    moveRobot(shape)
