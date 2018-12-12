import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from eval_tiny_one_image import *


def same(box1,box2):
    xi1 = max(box1[0], box2[0])
    yi1 = max(box1[1], box2[1])
    xi2 = min(box1[2]+box1[0], box2[2]+box2[0])
    yi2 = min(box1[3]+box1[1], box2[3]+box2[1])
    inter_area = max(xi2-xi1, 0)*max(yi2-yi1,0)
    box1_area = (box1[2])*(box1[3])
    box2_area = (box2[2])*(box2[3])
    union_area = box1_area + box2_area - inter_area
    iou = inter_area/union_area
    return iou

cap = cv2.VideoCapture("test_track.mp4")
if not cap.isOpened():
    print("Could not open video")
    sys.exit()
total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
duration = int(total_frame/fps)
bboxes = [[] for i in range(duration)]
dwelling = [[] for i in range(duration)]

for t in range(duration):
    print("Currently at t = " + str(t))
    # Read video
    cap = cv2.VideoCapture("test_track.mp4")
    cap.set(cv2.CAP_PROP_POS_FRAMES, t*fps)
    ok, frame = cap.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    frame = cv2.resize(frame,(int(cap.get(3)/2),int(cap.get(4)/2)))
    
    faces = main(frame)
    faces[:,2] = faces[:,2] - faces[:,0]
    faces[:,3] = faces[:,3] - faces[:,1]
    
    if (t > 0) & (len(faces) != 0):
        ind = []
        for i in range(faces.shape[0]):
            for j in range(len(bboxes[t-1])):
                if same(faces[i],bboxes[t-1][j]) > 0.4:
                    ind.append(i)
        ind = [i for i in range(faces.shape[0]) if i not in ind]
        faces = faces[ind]
    print(str(len(faces)) + " new faces found")
    
    if len(faces) > 0:
        fig,ax = plt.subplots(figsize = (8,4))
        display = np.zeros(frame.shape, dtype = "uint8")
        display[:,:,2] = frame[:,:,0]
        display[:,:,1] = frame[:,:,1]
        display[:,:,0] = frame[:,:,2]
        ax.imshow(display)
        for face in faces:
            rect = patches.Rectangle((face[0],face[1]),face[2],face[3],linewidth=1,edgecolor='r',facecolor='none')
            ax.add_patch(rect)
        plt.show()
    
    for f in range(len(faces)):
        print("tracking face " + str(f))
        bbox = (faces[f][0],faces[f][1],faces[f][2],faces[f][3])
         
        tracker = cv2.TrackerKCF_create()
        
        # Initialize tracker with first frame and bounding box
        capi = cv2.VideoCapture("test_track.mp4")
        capi.set(cv2.CAP_PROP_POS_FRAMES, t*fps)
        ok , frami = capi.read()
        frami = cv2.resize(frami,(int(capi.get(3)/2),int(capi.get(4)/2)))
        ok = tracker.init(frami, bbox)
        count = 0
        patience = 0
        for i in range(t*fps+1,total_frame):
            # Read a new frame
            ok, frami = capi.read()
            if not ok:
                print("frame reading problem at frame " + str(i)) # frame range from 0 to 459
                break
            frami = cv2.resize(frami,(int(capi.get(3)/2),int(capi.get(4)/2)))
            # Update tracker
            ok, bbox = tracker.update(frami)
            
            if ok:
                count += 1
                patience = 0
                if i%fps == 0:
                    bboxes[int(i/fps)-1].append(bbox)
            if not ok:
                patience += 1
                if patience > 3*fps:
                    break
        dwelling[t].append(count/fps)
    print("-----------------")
        

