# Finding unique faces

## Introduction

- The project consist of finding the number of unique faces appearing in a video.
- It allows one to know the time each face is appearing.
- Two technologies is combined to solve this problematic: face detection and object tracking.
- The face detection algorithm is from a research paper published in the CPVR 2017 by Peiyun Hu and Deva Ramanan. [link to paper](https://arxiv.org/abs/1612.04402) and [link to github](https://github.com/peiyunh/tiny). The version of detector in this project written in tensorflow is forked from the work of [cydonia999](https://github.com/cydonia999/Tiny_Faces_in_Tensorflow).
- The tracking system is a KCF tracker available in openCV. [Here](https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/) is a general introduction to object tracking in openCV    

## Technologies demonstration

- Face detection

![outi](https://user-images.githubusercontent.com/34350063/49846728-a8803200-fe07-11e8-897f-2084d2d6b984.jpg)

- Object tracking

![ezgif com-video-to-gif 1](https://user-images.githubusercontent.com/34350063/49845896-a3b97f00-fe03-11e8-9ed0-06590626bf96.gif)

## Methodology

- Example video of 20 seconds, 23 FPS, 460 frames.
- Run detection on first frame.
- Track a face through entire video, save tracker window every seconds (every 23 frames).
- Run detection on the 23th frame, compare IoU of detection window and tracker window.
- If IoU is low or null, a new face appeared and proceed to track it.
- Run detection on 46th frame, repeat previous comparison and continue so on until end of video.


