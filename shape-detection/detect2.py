from Utils.shapedetector import ShapeDetector
import argparse
from Utils import Utils
import cv2

capture = cv2.VideoCapture(0)

while True:

    has_frame, frame = capture.read()
    if not has_frame:
	    print('Can\'t get frame')
	    break

    resized = Utils.resize(frame, width=300)
    ratio = frame.shape[0] / float(resized.shape[0])
    '''
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    '''

    #'''
    blurred = cv2.GaussianBlur(resized, (5, 5), 0)
    cframe = cv2.Canny(blurred, 200,100)
    cnts = cv2.findContours(cframe.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #'''
    cnts = cnts[1]
    #print (cnts)
    sd = ShapeDetector()
    
    if len(cnts) > 0:
        for c in cnts:
	        M = cv2.moments(c)

	        if M["m00"] * ratio == 0:
	        	continue

	        cX = int((M["m10"] / M["m00"]) * ratio)
	        cY = int((M["m01"] / M["m00"]) * ratio)
	        shape = sd.detect(c)

	        c = c.astype("float")
	        c *= ratio
	        c = c.astype("int")
	        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
	        cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		        0.5, (255, 255, 255), 2)

	        cv2.imshow("Image", frame)

    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed Esc')
        break

capture.release()
cv2.destroyAllWindows()
