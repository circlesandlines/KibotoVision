import cv2
import brain

class MyBrain9000(brain.Brain):
	def think(self, imgdata):
                # process the image

		# make the image smaller so that processing is faster
		# change to quarter screen size
		derezzed = cv2.resize(imgdata, None, fx=0.25, fy = 0.25)
		print "screenshot derezzed"

                # analyze the image to gain some knowledge about the
                # player's situation
                gray = cv2.cvtColor(derezzed, cv2.COLOR_BGR2GRAY)
		print "enable grayscale"
                surf = cv2.xfeatures2d.SURF_create(10000)
		print "prime SURF algorithm"

                kp, des = surf.detectAndCompute(gray,None)
		print "execute SURF"

                # draw the points onto a new image
                processed = cv2.drawKeypoints(gray,kp,None,(255,0,0),4)
		print "draw detected points to window"

                # perform action (courtesy of pyautogui)
                # assuming some knowledge was gained form the analysis above
                # uncomment below to move a player forward and shoot in an FPS game
                #self.pag.press('up')
                #self.pag.click()

                # print the processed frame
                self._debug(processed)


if __name__=="__main__":
	b = MyBrain9000(fps=30)
	b.see()
