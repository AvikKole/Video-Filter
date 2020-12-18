import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow("filter")
cv2.createTrackbar("Blue","filter",0,255,nothing)
cv2.createTrackbar("Green","filter",0,255,nothing)
cv2.createTrackbar("Red","filter",0,255,nothing)
cv2.createTrackbar("Intensity","filter",1,10,nothing)
def apply_video_filter(filter):
    filter_h, filter_w, filter_c = filter.shape
    alpha=1
    bgra = (B,G,R,alpha)
    intensity=0.1*Intensity
    overlay = np.full((filter_h, filter_w, filter_c), bgra, dtype='uint8')#returns a new array of given shape,type & fill value
    cv2.addWeighted(overlay, intensity, filter, 1.0, 0, filter)# overlay-src1,alpha-inensity=0.8,filter=src2,beta=1.0,gamma=0,dest-filter
    return filter
while True:
    _,filter=cap.read()
    B=cv2.getTrackbarPos("Blue","filter")
    G=cv2.getTrackbarPos("Green","filter")
    R=cv2.getTrackbarPos("Red","filter")
    Intensity=cv2.getTrackbarPos("Intensity","filter")
    filter = cv2.cvtColor(filter, cv2.COLOR_BGR2BGRA)
    filter = apply_video_filter(filter.copy())
    cv2.imshow('filter',filter)
    #print(alpha)
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
    
