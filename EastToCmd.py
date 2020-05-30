#! encoding: UTF-8
import os
import cv2
video_full_path = "~/badapple.mp4"
cap = cv2.VideoCapture(video_full_path)
frame_count = 1
success = True
while(success):
    success, frame = cap.read()
    if  success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        s = ''
        for r in range(0, 360, 6):
            for c in range(0, 480, 3):
                if gray[r, c] > 200:
                    s += ' '
                else:
                    s += '0'
            s += '\n'
        print(s)
    params = []
    params.append(1)
    frame_count = frame_count + 1
cap.release()
