import numpy as np
import cv2

# 播放影片
#cap = cv2.VideoCapture(r'D:/Python_code/opencv/影片.mov')
# 讀取IP Camera內容
#cap = cv2.VideoCapture('http://192.168.0.137:81/videostream.cgi?loginuse=username&loginpas=password&resolution=32')
cap = cv2.VideoCapture('rtsp://admin:@@aten168@10.0.128.82:554/')
# 以迴圈從影片檔案讀取影格，並顯示出來
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lower_blue=np.array([0,43,46])
    upper_blue=np.array([180,255,255])
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    #cv2.imshow("res",res)
    #cv2.imshow('frame', gray)
    cv2.imshow('frame', frame)
    cv2.imwrite("result1.jpg",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()