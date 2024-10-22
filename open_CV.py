import numpy as np
import cv2

# 載入分類器
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('C:\\Users\\RayLin\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\cv2\~ata\\haarcascade_frontalface_default.xml')
# 讀取圖檔
img = cv2.imread(r'D:/Python_code/opencv/d3188140.jpg')
# 轉成灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測臉部
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4,
    minSize=(30, 30))
# 繪製人臉部份的方框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#(0, 255, 0)欄位可以變更方框顏色(Blue,Green,Red)
# 顯示成果
# cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
cv2.imshow('img', img)                     #秀出圖片
# cv2.imwrite( "result.jpg", img )           #保存圖片
cv2.waitKey(0)                             #等待按下任一按鍵
cv2.destroyAllWindows()                    #關閉視窗



# 顯示圖檔，第一個是視窗名稱，第二個是圖檔變數
# cv2.imshow('My Image',gray)
# 等待時間，0表示持續
# cv2.waitKey(0)
# 按下任何見關閉所有openCV視窗
# cv2.destroyAllWindows()
