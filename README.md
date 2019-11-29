# Finding unique faces

## Introduction

- The project consist of finding the number of unique faces appearing in a video.
- It allows one to know the time each face is appearing.
- Two technologies is combined to solve this problematic: face detection and object tracking.
- The face detection algorithm is from a research paper published in the CVPR 2017 by Peiyun Hu and Deva Ramanan. [link to paper](https://arxiv.org/abs/1612.04402) and [link to github](https://github.com/peiyunh/tiny). The version of detector in this project written in tensorflow is forked from the work of [cydonia999](https://github.com/cydonia999/Tiny_Faces_in_Tensorflow).
- The tracking system is a KCF tracker available in openCV. [Here](https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/) is a general introduction to object tracking in openCV    

## Demonstration

- Face detection

![outi](https://user-images.githubusercontent.com/34350063/49852875-4ed83180-fe20-11e8-83d0-792d275331e1.jpg)

- Object tracking

![ezgif com-video-to-gif 1](https://user-images.githubusercontent.com/34350063/49845896-a3b97f00-fe03-11e8-9ed0-06590626bf96.gif)

## Software Environment
- Python 3.6.6
- Tensorflow 1.11.0
- openCV 3.4.4

## Getting started
Install the necessary libraries
```bash
pip install -r requirements.txt
```
Download original matlab [weights](https://www.cs.cmu.edu/%7Epeiyunh/tiny/hr_res101.mat) and convert it to pickle file with 
```bash
python matconvnet_hr101_to_pickle.py
```
To track faces in video run:
```bash
python tracking.py
```
## Methodology
The tracking algorithm work as follow:
- Face detection is run on the first frame of the video.
- For each detected face, track it through the entire video (and save the tracker window at every seconds).
- Run face detection every second and compare IoU of detection window and tracker window.
- If IoU is low or null, a new face appeared and proceed to track it.


