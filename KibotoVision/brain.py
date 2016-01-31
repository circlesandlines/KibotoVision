import pyscreenshot as ImageGrab
import numpy
IMLIB = 'cv2'
try:
	raise
	import imlib as imlib
except:
	import skimage as imlib
	import matplotlib
	import matplotlib.pyplot as plt

	IMLIB = 'skimage'

import time
import pyautogui

import traceback

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
		if IMLIB == 'cv2':
			imlib.namedWindow('DebugVision', imlib.WINDOW_OPENGL)
		self.pag = pyautogui
		self.pag.FAILSAFE = True

	def _debug(self, img):
		if IMLIB == 'cv2':
			imlib.imshow('DebugVision', img)
		elif IMLIB == 'skimage':
			imlib.io.imshow(img, cmap=plt.cm.gray)

	def think(self, imgdata):
		"""Override this function for bot logic"""
		self._debug(imgdata)

	def start_bot(self):
		"""This method captures frames and executes the brain processor"""

		while(True):

			# wait for fps counting
			time.sleep(1/self.fps)

			# grab a screenshot
			im = ImageGrab.grab().convert('RGB')
			numpy_image = numpy.array(im) 
			# Convert RGB to BGR 
			numpy_image = numpy_image[:, :, ::-1].copy() 

			try:
				# execute the brain code
				self.think(numpy_image)

				if IMLIB == 'cv2':
					if imlib.waitKey(1) & 0xFF == ord('q'):
						break

			except Exception as e:
				traceback.print_exc()

		imlib.destroyAllWindows()
