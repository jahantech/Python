import numpy as np
import cv2

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


cap = cv2.VideoCapture('Sample2.mp4')
count = 0
Sensitivity = 1 * 2000 
i = 0
NewVideoFrame=0
fps    = cap.get(cv2.cv.CV_CAP_PROP_FPS)
LengthofFrames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
print fps
print LengthofFrames
fourcc = cv2.cv.CV_FOURCC(*'DIVX')
while cap.isOpened():
    ret,frame = cap.read()
    width = 1080
    height = 720
    
    if i == 0:
        video = cv2.VideoWriter('gifart.avi',fourcc,fps,(width,height))
        InitialFrame = frame
        cv2.imshow('window-name',frame)
        cv2.imwrite("frame%d.jpg" % count, frame)
    elif i < LengthofFrames:
        mseval = mse(frame,InitialFrame)
        if mseval > Sensitivity:
            cv2.imshow('window-name',frame)
            cv2.imwrite("frame%d.jpg" % count, frame)
            InitialFrame = frame
            print count 
            print mseval 
            video.write(frame)
    count = count + 1
    i = i + 1
video.release 
cap.release()

