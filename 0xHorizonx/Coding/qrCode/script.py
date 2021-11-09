#!/usr/bin/env python3
import cv2

PATH = "./images/"
NB_FRAMES = 44

result = ""
for i in range(NB_FRAMES):
    if i<10:
        img=cv2.imread(PATH+f"frame_0{i}_delay-0.2s.jpg")
    else:
        img=cv2.imread(PATH+f"frame_{i}_delay-0.2s.jpg")
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    result+=val
print(result)