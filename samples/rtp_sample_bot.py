import cv2
from brain import brain_rtp

class Mybot9000(brain_rtp.Brain):
	def brain(self, imgdata):
		# process the image

		# analyze the image to gain some knowledge about the
		# player's situation
		gray = cv2.cvtColor(imgdata, cv2.COLOR_BGR2GRAY)
		surf = cv2.xfeatures2d.SURF_create(5000)

		kp, des = surf.detectAndCompute(gray,None)

		# draw the points onto a new image
		processed = cv2.drawKeypoints(gray,kp,None,(255,0,0),4)

		# perform action (courtesy of pyautogui)
		# assuming some knowledge was gained form the analysis above
		# uncomment below to move a player forward and shoot in an FPS game
		#self.pag.press('up')
		#self.pag.click()

		# print the processed frame
		self._debug(processed)

if __name__=="__main__":
	bot = Mybot9000()
	bot.see()
