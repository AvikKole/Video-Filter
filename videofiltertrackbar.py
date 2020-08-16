import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow("filter")
cv2.createTrackbar("B","filter",0,255,nothing)
cv2.createTrackbar("G","filter",0,255,nothing)
cv2.createTrackbar("R","filter",0,255,nothing)
def apply_video_filter(filter, intensity=0.5):
    filter_h, filter_w, filter_c = filter.shape
    alpha=1
    bgra = (B,G,R,alpha)
    overlay = np.full((filter_h, filter_w, filter_c), bgra, dtype='uint8')#returns a new array of given shape,type & fill value
    cv2.addWeighted(overlay, intensity, filter, 1.0, 0, filter)# overlay-src1,alpha-inensity=0.8,frame=src2,beta=1.0,gamma=0,dest-frame
    return filter
while True:
    _,filter=cap.read()
    B=cv2.getTrackbarPos("B","filter")
    G=cv2.getTrackbarPos("G","filter")
    R=cv2.getTrackbarPos("R","filter")
    filter = cv2.cvtColor(filter, cv2.COLOR_BGR2BGRA)
    filter = apply_video_filter(filter.copy())
    #cv2.imshow('frame',frame)
    cv2.imshow('filter',filter)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
    
