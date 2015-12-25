#!/bin/bash
ffmpeg -y -framerate 5 -video_size 640x480 -f avfoundation -i "1:none" -vcodec libx264 -crf 0 -preset ultrafast stream/out.h264
