import pyscreenshot as ImageGrab
import numpy
IMLIB = 'cv2'
try:
	raise
	import cv2 as imlib
except:
	import skimage as imlib
	import matplotlib.animation as animation
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
		self.imlib = IMLIB
		if IMLIB == 'cv2':
			imlib.namedWindow('DebugVision', imlib.WINDOW_OPENGL)
		elif IMLIB == 'skimage':
			self.window = plt.figure()
			self.plt_image = None
			self.anim = None
			self.frame_num = 0

		self.pag = pyautogui
		self.pag.FAILSAFE = True

		# create a debug frame

	def _debug(self, img):
		if IMLIB == 'cv2':
			imlib.imshow('DebugVision', img)
		elif IMLIB == 'skimage':
			# can't just show the image like this
			# need to integrate with their stupid
			# animation function. skimage has bad
			# architecture... >:(
			#plt.imshow(img)
			#plt.axis('off')
			#plt.show()
			return

	def think(self, imgdata):
		"""Override this function for bot logic"""
		self._debug(imgdata)

	def _debug_think(self, *args):
		"""This method is provided to the matplot-lib's FuncAnimation function
		That will manage the framerate, displaying the debug window, or
		saving a debug movie. Only use this for debugging. Otherwise use
		start_bot()"""

		# grab a screenshot
		im = ImageGrab.grab().convert('RGB')
		numpy_image = numpy.array(im) 
		# Convert RGB to BGR 
		numpy_image = numpy_image[:, :, ::-1].copy() 

		try:
			# execute the brain code
			self.think(numpy_image)

		except Exception as e:
			traceback.print_exc()

		self.plt_image.set_array(numpy_image)
		self.frame_num += 1
		print("frame: %d" % self.frame_num)

		return self.plt_image,

	def start_bot_skimage(self):

		#prime the image buffer frame
		im = ImageGrab.grab().convert('RGB')
		self.plt_image = plt.imshow(im, animated=True)

		self.anim = animation.FuncAnimation(fig=self.window, func=self._debug_think, interval=1000.0/self.fps, blit=False)
		plt.show()

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
