import cv2 as cv
import numpy as np

# Provide your screen Path
vidcap = cv.VideoCapture(r'C:\Users\ashut\Desktop\OpenCV Projects\Opencv\Videos\TestVideo.mp4')

# Reading the Video
ret,image = vidcap.read()
count = 0
while True:
    if ret==True:
        cv.imwrite(r'C:\Users\ashut\Desktop\OpenCV Projects\Screen Recorder\Frames\img%d.jpg'%count,image)
        vidcap.set(cv.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv.imshow("Images",image)
        count+=1
        if cv.waitKey(1) & 0xFF==ord("q"):
                break
                cv.destroyAllWindows()

vidcap.release()
cv.destroyAllWindows()
