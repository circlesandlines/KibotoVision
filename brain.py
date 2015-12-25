import cv2, platform
import time

def brain(imgdata, fnum):
	# do image stuff here
	cv2.imshow('BotStream', imgdata)

capture = cv2.VideoCapture('stream/out.h264')
cv2.namedWindow('BotStream', cv2.WINDOW_OPENGL)

fnum = 0
while(True):

	(grabbed, imgdata) = capture.read()

	if not grabbed:
		print "no image"
		time.sleep(0.2)
		continue

	try:
		# execute the brain code
		brain(imgdata, fnum)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	except Exception as e:
		print "Frame display error: ", e
		time.sleep(0.2)
		continue

	fnum += 1
	time.sleep(0.2)

capture.release()
cv2.destroyAllWindows()
