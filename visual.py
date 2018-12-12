import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from eval_tiny_one_image import *

cap = cv2.VideoCapture("test_track.mp4")
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920,1080))
cap.set(cv2.CAP_PROP_POS_FRAMES, 0*23)
if not cap.isOpened():
    print("Could not open video")
    sys.exit()
    
ok, frame = cap.read()
if not ok:
    print('Cannot read video file')
    sys.exit()
frame = cv2.resize(frame,(400,230))

faces = main(frame)
faces[:,2] = faces[:,2] - faces[:,0]
faces[:,3] = faces[:,3] - faces[:,1]
    
#faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#faces = faceCascade.detectMultiScale(
#                    gray,
#                    scaleFactor = 1.2,
#                    minNeighbors = 3,
#                    minSize=(10, 10))

fig,ax = plt.subplots(figsize = (16,10))
display = np.zeros(frame.shape, dtype = "uint8")
display[:,:,2] = frame[:,:,0]
display[:,:,1] = frame[:,:,1]
display[:,:,0] = frame[:,:,2]
ax.imshow(display)
for face in faces:
    rect = patches.Rectangle((face[0],face[1]),face[2],face[3],linewidth=1,edgecolor='b',facecolor='none')
    ax.add_patch(rect)
plt.show()   

f = 1
bbox = (faces[f][0],faces[f][1],faces[f][2],faces[f][3])

tracker = cv2.TrackerKCF_create()
ok = tracker.init(frame, bbox)

for i in range(200):    
    ok, frame = cap.read()
    if not ok:
        break
    #frame = cv2.resize(frame,(int(cap.get(3)/2),int(cap.get(4)/2)))
    timer = cv2.getTickCount()
    # Update tracker
    ok, bbox = tracker.update(frame)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    # Draw bounding box
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
    # Display tracker type on frame
    cv2.putText(frame, "KCF" + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
 
    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
    #out.write(frame)
    ## Display result
    cv2.namedWindow('Tracking',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Tracking', 1000,600)
    cv2.imshow("Tracking", frame)
    
    k = cv2.waitKey(1) & 0xff
    if k == 27: 
        break
