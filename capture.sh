#!/bin/bash
ffmpeg -y -framerate 10 -async 1 -pix_fmt uyvy422 -s 1280x800 -threads 2 -f avfoundation -i "1:none" -vcodec libx264 -tune zerolatency -preset ultrafast -crf 0 -vf scale=640:-1 stream/out.h264
