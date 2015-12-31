
import brain

class MyBrain9000(brain.Brain):
	def think(self, imgdata):
		self._debug(imgdata)

if __name__=="__main__":
	b = MyBrain9000(fps=30)
	b.see()
