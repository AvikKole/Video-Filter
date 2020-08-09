import numpy as np
import cv2
cap = cv2.VideoCapture(0)
blue=input("Enter blue pixel intensity :")
green=input("Enter green pixel intensity :")
red=input("Enter red pixel intensity :")
def verify_alpha_channel(frame):
    try:
        frame.shape[3] # looking for the alpha channel
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame
def apply_video_filter(frame, intensity=0.5):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    alpha=1
    bgra = (blue,green,red,alpha)
    overlay = np.full((frame_h, frame_w, frame_c), bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)# overlay-src1,alpha-inensity=0.8,frame=src2,beta=1.0,gamma=0,dest-frame
    return frame
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    filter = apply_video_filter(frame.copy())
    cv2.imshow('frame',frame)
    cv2.imshow('Video_filter',filter)
    k=cv2.waitKey(20) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()    
