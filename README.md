# KibotoVision

A version that allows bots to analyze a live stream of the game for decision making.
Built with OpenCV and ffmpeg.

## Requirements
- Python 2.x or 3.x
- Python OpenCV 3
- pyautogui
- ffmpeg

## Usage
Simply extent the Brain class in **brain_rtp.py** and override the **brain** function.
Check the **sample_bot.py** file for an example.

**Note:** pyautogui has a failsafe feature, so that when your keyboard and mouse actions backfire, you can cancel the actions by moving the mouse to the top right. The Brain class enables this by default.

## Notes:
- Check out the `capture_rtp.sh` file for adjusting framerate and stream quality
- for pyautogui usage, check the sample bot, as well as the [documentation](https://pyautogui.readthedocs.org/en/latest/introduction.html)
- for lots of modern OpenCV tutorials, check out this [blog](http://www.pyimagesearch.com/)
