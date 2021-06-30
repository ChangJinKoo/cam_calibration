import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
count = 1

while(1):
	ret, frame = cam.read()
	if not ret:
		print("Webcam read error!")
		break
	cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)
	cv2.imshow("video", frame)
	k = cv2.waitKey(1)
	
	if k == 27:
		break
	elif k == ord('s'):		# Push 's' then you can store camera images
		cv2.imwrite('xx' + str(count) + '.jpg', frame)
		count += 1
		if count == 9:
			break

cam.release()
cv2.destroyAllwindows()
