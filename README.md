# KibotoVision

Kiboto Vision allows you to develop AI bots that play any game by defining an interface on top of a video stream of the game.
Built with OpenCV. For an alternative that doesn't work by analyzing a video stream, see [Kiboto](http://kiboto.com/).

## Requirements
- Python 2.x or 3.x
- matplotlib
- scikit-image
- pyscreenshot
- pyautogui

## Installation
```bash
python setup.py install
```

## Usage
simply follow the example in the **pil_sample_bot.py file**. Specify the fps and brain logic, then run with `python pil_sample_bot.py`.
The example below implements a SURF feature detection algorithm as an example.

```python
import cv2
from KibotoVision import brain

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
		# self.pag.press('up')
		# self.pag.click()

		# print the processed frame
		self._debug(processed)


if __name__=="__main__":
	b = MyBrain9000(fps=30)
	b.start_bot()
```

**Note:** pyautogui has a failsafe feature, so that when your keyboard and mouse actions backfire, you can cancel the actions by moving the mouse to the top right. The Brain class enables this by default.

## Notes:
- for pyautogui usage, check the sample bot, as well as the [documentation](https://pyautogui.readthedocs.org/en/latest/introduction.html)
- for lots of modern OpenCV tutorials and great install instructions, check out this [blog](http://www.pyimagesearch.com/)
- if matplot lib generates [this error](https://github.com/matplotlib/matplotlib/issues/5836), just run the following command:
```bash
rm -rf ~/.matplotlib/fontList.cache
```
- parts of the matplotlib animation implementation can be [found here](https://github.com/aizvorski/scikit-video/blob/master/skvideo/examples/player.py
