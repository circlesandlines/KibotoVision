import cv2, platform
import time

"""
	Extend Brain class so you can implement your own brain logic
	Just override the brain method

	TODO:
	- need to add the moust and keyboard control aspect of the SDK

"""

class Brain:
	def __init__(self):
		self.capture = cv2.VideoCapture('stream.sdp')
		cv2.namedWindow('DebugVision', cv2.WINDOW_OPENGL)

	def _debug(self, img):
		cv2.imshow('DebugVision', img)

	def brain(self, imgdata):
		"""Override this function for bot logic"""
		self._debug(imgdata)

	def see(self):
		"""This method captures frames and executes the brain processor"""

		while(True):
			(grabbed, imgdata) = self.capture.read()

			if not grabbed:
				# no frame data captured
				continue

			try:
				# execute the brain code
				self.brain(imgdata)

				if cv2.waitKey(1) & 0xFF == ord('q'):
					break

			except Exception as e:
				print "Frame processing error: ", e
				continue

		self.capture.release()
		cv2.destroyAllWindows()
