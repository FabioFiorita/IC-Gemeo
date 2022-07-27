import cv2

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