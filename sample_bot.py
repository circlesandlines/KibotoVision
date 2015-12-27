import cv2
import brain_rtp

class Mybot9000(brain_rtp.Brain):
	def brain(self, imgdata):
		# process the image

		# grayscale image for example
		gray = cv2.cvtColor(imgdata, cv2.COLOR_BGR2GRAY)

		self._debug(gray)

if __name__=="__main__":
	bot = Mybot9000()
	bot.see()
