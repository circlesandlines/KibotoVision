import pyscreenshot as ImageGrab
import numpy
import cv2
import time
import pyautogui

"""
	Extend Brain class so you can implement your own brain logic
	Just override the brain method

	TODO:
	- need to add the moust and keyboard control aspect of the SDK

"""

class Brain:
	def initialize(self, kv_dict={}):
		"""Override this method to initialize your bot in whatever
		way you'd like"""

	def __init__(self, fps=15):
		self.fps = fps
		cv2.namedWindow('DebugVision', cv2.WINDOW_OPENGL)
		self.pag = pyautogui
		self.pag.FAILSAFE = True

	def _debug(self, img):
		cv2.imshow('DebugVision', img)

	def think(self, imgdata):
		"""Override this function for bot logic"""
		self._debug(imgdata)

	def see(self):
		"""This method captures frames and executes the brain processor"""

		while(True):

			# wait for fps counting
			time.sleep(1/self.fps)

			# grab a screenshot
			im = ImageGrab.grab().convert('RGB')
			open_cv_image = numpy.array(im) 
			# Convert RGB to BGR 
			open_cv_image = open_cv_image[:, :, ::-1].copy() 

			try:
				# execute the brain code
				self.think(open_cv_image)

				if cv2.waitKey(1) & 0xFF == ord('q'):
					break

			except Exception as e:
				print "Frame processing error: ", e
				continue

		cv2.destroyAllWindows()
