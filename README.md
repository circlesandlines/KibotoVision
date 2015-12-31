# KibotoVision

A version that allows bots to analyze a live stream of the game for decision making.
Built with OpenCV and ffmpeg.

## Requirements
- Python 2.x or 3.x
- Python OpenCV 3
- pyscreenshot
- pyautogui
- ffmpeg

## Usage
There are two versions. The pyscreenshot version which simply takes a screengrab at the desired fps using PIL; and the rtmp streaming version that basically creates a live video stream. The rtmp version is **slower** than the pyscreenshot version, it isn't recommended.

### pyscreenshot Version
simply follow the example in the **pil_sample_bot.py file**. Specify the fps and brain logic, then simply run with `python pil_sample_bot.py`.

### RTP stream
There is a bit of lag with this technique depending on your hardware. Simply extent the Brain class in **brain_rtp.py** and override the **brain** function.
Check the **sample_bot.py** file for an example.

**Note:** pyautogui has a failsafe feature, so that when your keyboard and mouse actions backfire, you can cancel the actions by moving the mouse to the top right. The Brain class enables this by default.

## Notes:
- Check out the `capture_rtp.sh` file for adjusting framerate and stream quality
- for pyautogui usage, check the sample bot, as well as the [documentation](https://pyautogui.readthedocs.org/en/latest/introduction.html)
- for lots of modern OpenCV tutorials and great install instructions, check out this [blog](http://www.pyimagesearch.com/)
