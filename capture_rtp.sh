#!/bin/bash
ffmpeg -y -framerate 15 -f avfoundation -i "1:none" -vcodec libx264 -preset ultrafast -vf scale=640:-1 -f mulaw -f rtp rtp://127.0.0.1:1234
