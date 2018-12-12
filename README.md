## Face-detection-and-tracking

# Introduction

- The project consist of finding the number of unique faces appearing in a video.
- It allows one to know the time each face is appearing.
- Two technologies is combined to solve this problematic: face detection and object tracking.
- The face detection algorithm is from a research paper published in the CPVR 2017 by Peiyun Hu and Deva Ramanan. link to paper:             https://arxiv.org/abs/1612.04402, link to github: https://github.com/peiyunh/tiny. The version of detector in this project is written in   tensorflow forked from the work of cydonia999: https://github.com/cydonia999/Tiny_Faces_in_Tensorflow.
- The tracking system is a KCF tracker available in openCV. Here is a general introduction to object tracking in openCV https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/   
